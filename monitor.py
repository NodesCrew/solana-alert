# coding: utf-8
import config
import asyncio


from lib.solana import SolanaCluster
from lib.logging import get_logger


loop = asyncio.get_event_loop()
logger = get_logger("simple-monitor")


async def main():
    bad_nodes = []

    for cluster_name in config.CLUSTERS:
        if not config.CLUSTERS[cluster_name]["nodes"]:
            continue

        cluster = SolanaCluster(cluster_name, **config.CLUSTERS[cluster_name])
        nodes = await cluster.collect_info()

        len_nodes_config = len(config.CLUSTERS[cluster_name]["nodes"])
        len_nodes_cluster = len(nodes)

        if len_nodes_config < len_nodes_cluster:
            logger.warning(f"Not all nodes found in cluster! "
                           f"Nodes in config: {len_nodes_config}, "
                           f"nodes in cluster: {len_nodes_cluster}")

        for node in nodes:
            if node.is_delinquent:
                cluster.logger.warning(f"Node {node.node_pk} is delinquent!")
                bad_nodes.append(node)

            elif node.vote_diff > cluster.max_vote_diff:
                cluster.logger.warning(
                    f"Node {node.name} vote diff is too high! "
                    f"Node diff: {node.vote_diff}, "
                    f"max cluster diff: {cluster.max_vote_diff}")
                bad_nodes.append(node)

            elif node.identity_balance < cluster.min_node_balance:
                cluster.logger.warning(
                    f"Node {node.name} balance is too small! "
                    f"Node balance: {node.identity_balance}, "
                    f"min cluster balance: {cluster.min_node_balance}")
                bad_nodes.append(nodes)

            else:
                cluster.logger.info(f"Node {node.name} is working good")


if __name__ == "__main__":
    if __name__ == "__main__":
        try:
            srv = loop.run_until_complete(main())
        except KeyboardInterrupt:
            loop.close()
