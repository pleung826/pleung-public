from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import ECS, EKS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB, TransitGateway, VPC
from diagrams.aws.network import Route53

from diagrams import Cluster, Diagram
from diagrams.aws.analytics import ManagedStreamingForKafka
# from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub
# from diagrams.gcp.compute import AppEngine, Functions
# from diagrams.gcp.database import BigTable
# from diagrams.gcp.iot import IotCore
# from diagrams.gcp.storage import GCS


with Diagram("EKS and Kafka diagram", show=False, direction="TB"):

    with Cluster("TGW "):
        tgw=TransitGateway("EKS TGW")
        tgw_prisma=TransitGateway("Primsa")
        tgw_internet_vpc=TransitGateway("Internet VPC")
        tgw_simon=TransitGateway("Simon VPC")
        [tgw, tgw_prisma, tgw_internet_vpc, tgw_simon]

    with Cluster("Confluent.io"):
        kafka_prod = ManagedStreamingForKafka("Kafka prod")
        kafka_prod_dr = ManagedStreamingForKafka("Kafka prod_dr")
        kafka_staging = ManagedStreamingForKafka("Kafka staging")
        kafka_feature_staging = ManagedStreamingForKafka("Kafka feature staging")
        kafka_prod - Edge(color="brown", style="dashed") - kafka_prod_dr


    with Cluster("Confluent.io - Dedicated Kafka"):
        dedicated_kafka_prod = ManagedStreamingForKafka("Kafka prod")
        dedicated_kafka_prod_dr = ManagedStreamingForKafka("Kafka prod_dr")
        dedicated_kafka_prod_eu = ManagedStreamingForKafka("Kafka prod eu")
        dedicated_kafka_prod_eu_dr = ManagedStreamingForKafka("Kafka prod_eu_dr")
        dedicated_kafka_prod - Edge(color="brown", style="dashed") - dedicated_kafka_prod_dr
        dedicated_kafka_prod_eu - Edge(color="brown", style="dashed") - dedicated_kafka_prod_eu_dr

        dedicated_kafka_prod >> Edge(color="darkgreen")  << tgw
        dedicated_kafka_prod_dr >> Edge(color="darkgreen")  << tgw
        dedicated_kafka_prod_eu >> Edge(color="darkgreen")  << tgw
        dedicated_kafka_prod_eu_dr >> Edge(color="darkgreen")  << tgw


    with Cluster("All infra"):
        with Cluster("Simon Infra "):
            with Cluster("Production AWS Account"):
                with Cluster("VPC production 10.1.2.3/16"):
                    eks_simon_production = EKS("production")
            with Cluster("QA AWS Account"):
                with Cluster("VPC QA 10.1.2.3/16"):
                    eks_simon_qa = EKS("qa")
            with Cluster("Alpha AWS Account"):
                with Cluster("VPC Alpha 10.1.2.3/16"):
                    eks_simon_alpha = EKS("alpha")


            tgw >>  Edge(color="darkgreen") << eks_simon_production
            tgw >>  Edge(color="darkgreen") << eks_simon_alpha
            tgw >>  Edge(color="darkgreen") << eks_simon_qa


        with Cluster("ICN AWS"):
            with Cluster("Production AWS Account"):
                with Cluster("Prod VPC 10.1.2.3/16"):
                    eks_prod = EKS("prod")
                    tgw >> eks_prod
                    kafka_prod >>  Edge(color="darkgreen") << tgw_internet_vpc
                with Cluster("VPC prod-dr 10.1.2.3/16"):
                    eks_prod_dr = EKS("prod-dr")
                    tgw >> eks_prod_dr
                with Cluster("VPC prod-eu 10.1.2.3/16"):
                    eks_prod_eu = EKS("prod-eu")
                    tgw >> eks_prod_eu
                with Cluster("VPC prod-eu-dr 10.1.2.3/16"):
                    eks_prod_eu_dr = EKS("prod-eu-dr")
                    tgw >> Edge(color="darkgreen") << eks_prod_eu_dr
                eks_prod - Edge(color="brown", style="dashed") - eks_prod_dr
                eks_prod_eu - Edge(color="brown", style="dashed") - eks_prod_eu_dr

            with Cluster("UAT AWS Account"):
                with Cluster("VPC uat 10.1.2.3/16"):
                    eks_uat = EKS("uat")
                    tgw >> Edge(color="darkgreen")  << eks_uat

            with Cluster("Staging AWS Account"):
                with Cluster("VPC staging 10.1.2.3/16"):
                    eks_staging = EKS("staging")
                    tgw >> eks_staging
                    kafka_staging >>  Edge(color="darkgreen") << tgw_internet_vpc
                with Cluster("VPC staging-eu 10.1.2.3/16"):
                    eks_staging_eu = EKS("staging_eu")
                    tgw >> Edge(color="darkgreen")  << eks_staging_eu
                with Cluster("VPC feature-staging 10.1.2.3/16"):
                    eks_fs = EKS("feature-staging")
                    tgw >> Edge(color="darkgreen") << eks_fs


