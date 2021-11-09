# coding: utf-8
import asyncio
import aiohttp

from dataclasses import dataclass

from lib.logging import get_logger
from lib.solana_rpc import get_balance
from lib.solana_rpc import get_epoch_info
from lib.solana_rpc import get_vote_accounts


@dataclass
class SolanaNode:
    name: str
    cluster: str
    node_pk: str
    vote_pk: str
    last_vote: int
    vote_diff: int
    is_delinquent: bool
    identity_balance: float


class SolanaCluster(object):
    __slots__ = ("logger", "nodes", "cluster_name", "rpc_url",
                 "max_vote_diff", "min_node_balance")

    def __init__(self,
                 cluster_name: str,
                 rpc_url: str,
                 nodes: dict,
                 max_vote_diff: int,
                 min_node_balance: float):
        self.nodes = nodes
        self.logger = get_logger(cluster_name)
        self.rpc_url = rpc_url
        self.cluster_name = cluster_name
        self.max_vote_diff = max_vote_diff
        self.min_node_balance = min_node_balance

    async def collect_info(self) -> list[SolanaNode]:
        """ Collect blockchain information
        """
        self.logger.debug("Grab data from cluster")
        async with aiohttp.ClientSession() as http:
            tasks = [get_epoch_info(http=http, cluster_rpc=self.rpc_url),
                     get_vote_accounts(http=http, cluster_rpc=self.rpc_url)]
            epoch_info, vote_accounts = await asyncio.gather(*tasks)
        # self.logger.debug(f"Epoch info: {epoch_info}")

        abs_slot = epoch_info["absoluteSlot"]
        our_nodes = []

        for state, nodes in vote_accounts.items():
            for node in nodes:
                if node["nodePubkey"] not in self.nodes:
                    continue

                node_pk = node["nodePubkey"]

                our_nodes.append(
                    SolanaNode(
                        name=self.nodes[node_pk],
                        cluster=self.cluster_name,
                        node_pk=node_pk,
                        vote_pk=node["votePubkey"],
                        last_vote=node["lastVote"],
                        vote_diff=abs_slot - node["lastVote"],
                        is_delinquent=state == "delinquent",
                        identity_balance=0,
                    )
                )

        our_nodes = await self.update_balances(our_nodes)
        return our_nodes

    async def update_balances(self, nodes):
        async with aiohttp.ClientSession() as http:
            tasks = [get_balance(http, self.rpc_url, node.node_pk)
                     for node in nodes]
            balances = await asyncio.gather(*tasks)

        for idx, balance in enumerate(balances):
            nodes[idx].identity_balance = balance

        return nodes
