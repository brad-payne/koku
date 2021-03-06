# Generated by Django 2.2.11 on 2020-03-28 01:08
import django.contrib.postgres.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("reporting", "0106_ocpawscostsummary")]

    operations = [
        migrations.CreateModel(
            name="OCPAzureComputeSummary",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("usage_start", models.DateField()),
                ("usage_end", models.DateField()),
                ("cluster_id", models.CharField(max_length=50, null=True)),
                ("cluster_alias", models.CharField(max_length=256, null=True)),
                ("instance_type", models.CharField(max_length=50, null=True)),
                ("resource_id", models.CharField(max_length=253, null=True)),
                ("usage_quantity", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("unit_of_measure", models.CharField(max_length=63, null=True)),
                ("pretax_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("markup_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("currency", models.CharField(default="USD", max_length=10)),
            ],
            options={"db_table": "reporting_ocpocpazure_compute_summary", "managed": False},
        ),
        migrations.CreateModel(
            name="OCPAzureCostSummary",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("usage_start", models.DateField()),
                ("usage_end", models.DateField()),
                ("cluster_id", models.CharField(max_length=50, null=True)),
                ("cluster_alias", models.CharField(max_length=256, null=True)),
                ("pretax_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("markup_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("currency", models.CharField(default="USD", max_length=10)),
            ],
            options={"db_table": "reporting_ocpocpazure_cost_summary", "managed": False},
        ),
        migrations.CreateModel(
            name="OCPAzureCostSummaryByAccount",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("usage_start", models.DateField()),
                ("usage_end", models.DateField()),
                ("cluster_id", models.CharField(max_length=50, null=True)),
                ("cluster_alias", models.CharField(max_length=256, null=True)),
                ("subscription_guid", models.CharField(max_length=50)),
                ("pretax_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("markup_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("currency", models.CharField(default="USD", max_length=10)),
            ],
            options={"db_table": "reporting_ocpocpazure_cost_summary_by_account", "managed": False},
        ),
        migrations.CreateModel(
            name="OCPAzureCostSummaryByLocation",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("usage_start", models.DateField()),
                ("usage_end", models.DateField()),
                ("cluster_id", models.CharField(max_length=50, null=True)),
                ("cluster_alias", models.CharField(max_length=256, null=True)),
                ("resource_location", models.CharField(max_length=50)),
                ("pretax_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("markup_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("currency", models.CharField(default="USD", max_length=10)),
            ],
            options={"db_table": "reporting_ocpocpazure_cost_summary_by_location", "managed": False},
        ),
        migrations.CreateModel(
            name="OCPAzureCostSummaryByService",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("usage_start", models.DateField()),
                ("usage_end", models.DateField()),
                ("cluster_id", models.CharField(max_length=50, null=True)),
                ("cluster_alias", models.CharField(max_length=256, null=True)),
                ("service_name", models.TextField()),
                ("pretax_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("markup_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("currency", models.CharField(default="USD", max_length=10)),
            ],
            options={"db_table": "reporting_ocpocpazure_cost_summary_by_service", "managed": False},
        ),
        migrations.CreateModel(
            name="OCPAzureDatabaseSummary",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("usage_start", models.DateField()),
                ("usage_end", models.DateField()),
                ("cluster_id", models.CharField(max_length=50, null=True)),
                ("cluster_alias", models.CharField(max_length=256, null=True)),
                ("service_name", models.TextField()),
                ("usage_quantity", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("unit_of_measure", models.CharField(max_length=63, null=True)),
                ("pretax_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("markup_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("currency", models.CharField(default="USD", max_length=10)),
            ],
            options={"db_table": "reporting_ocpocpazure_database_summary", "managed": False},
        ),
        migrations.CreateModel(
            name="OCPAzureNetworkSummary",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("usage_start", models.DateField()),
                ("usage_end", models.DateField()),
                ("cluster_id", models.CharField(max_length=50, null=True)),
                ("cluster_alias", models.CharField(max_length=256, null=True)),
                ("service_name", models.TextField()),
                ("usage_quantity", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("unit_of_measure", models.CharField(max_length=63, null=True)),
                ("pretax_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("markup_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("currency", models.CharField(default="USD", max_length=10)),
            ],
            options={"db_table": "reporting_ocpocpazure_network_summary", "managed": False},
        ),
        migrations.CreateModel(
            name="OCPAzureStorageSummary",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("usage_start", models.DateField()),
                ("usage_end", models.DateField()),
                ("cluster_id", models.CharField(max_length=50, null=True)),
                ("cluster_alias", models.CharField(max_length=256, null=True)),
                ("service_name", models.TextField()),
                ("usage_quantity", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("unit_of_measure", models.CharField(max_length=63, null=True)),
                ("pretax_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("markup_cost", models.DecimalField(decimal_places=9, max_digits=24, null=True)),
                ("currency", models.CharField(default="USD", max_length=10)),
            ],
            options={"db_table": "reporting_ocpocpazure_storage_summary", "managed": False},
        ),
        migrations.RunSQL(
            """
            DROP MATERIALIZED VIEW IF EXISTS reporting_ocpazure_cost_summary
            ;

            CREATE MATERIALIZED VIEW reporting_ocpazure_cost_summary AS(
                SELECT row_number() OVER(ORDER BY usage_start, cluster_id, cluster_alias) as id,
                    usage_start as usage_start,
                    usage_start as usage_end,
                    cluster_id,
                    cluster_alias,
                    sum(pretax_cost) as pretax_cost,
                    sum(markup_cost) as markup_cost,
                    max(currency) as currency
                FROM reporting_ocpazurecostlineitem_daily_summary
                -- Get data for this month or last month
                WHERE usage_start >= DATE_TRUNC('month', NOW() - '1 month'::interval)::date
                GROUP BY usage_start, cluster_id, cluster_alias
            )
            ;

            CREATE UNIQUE INDEX ocpazure_cost_summary
            ON reporting_ocpazure_cost_summary (usage_start, cluster_id, cluster_alias)
            ;

            DROP MATERIALIZED VIEW IF EXISTS reporting_ocpazure_cost_summary_by_account
            ;

            CREATE MATERIALIZED VIEW reporting_ocpazure_cost_summary_by_account AS(
                SELECT row_number() OVER(ORDER BY usage_start, cluster_id, cluster_alias, subscription_guid) as id,
                    usage_start as usage_start,
                    usage_start as usage_end,
                    cluster_id,
                    cluster_alias,
                    subscription_guid,
                    sum(pretax_cost) as pretax_cost,
                    sum(markup_cost) as markup_cost,
                    max(currency) as currency
                FROM reporting_ocpazurecostlineitem_daily_summary
                -- Get data for this month or last month
                WHERE usage_start >= DATE_TRUNC('month', NOW() - '1 month'::interval)::date
                GROUP BY usage_start, cluster_id, cluster_alias, subscription_guid
            )
            ;

            CREATE UNIQUE INDEX ocpazure_cost_summary_account
            ON reporting_ocpazure_cost_summary_by_account (usage_start, cluster_id, cluster_alias, subscription_guid)
            ;

            DROP MATERIALIZED VIEW IF EXISTS reporting_ocpazure_cost_summary_by_location
            ;

            CREATE MATERIALIZED VIEW reporting_ocpazure_cost_summary_by_location AS(
                SELECT row_number() OVER(ORDER BY usage_start, cluster_id, cluster_alias, resource_location) as id,
                    usage_start as usage_start,
                    usage_start as usage_end,
                    cluster_id,
                    cluster_alias,
                    resource_location,
                    sum(pretax_cost) as pretax_cost,
                    sum(markup_cost) as markup_cost,
                    max(currency) as currency
                FROM reporting_ocpazurecostlineitem_daily_summary
                -- Get data for this month or last month
                WHERE usage_start >= DATE_TRUNC('month', NOW() - '1 month'::interval)::date
                GROUP BY usage_start, cluster_id, cluster_alias, resource_location
            )
            ;

            CREATE UNIQUE INDEX ocpazure_cost_summary_location
            ON reporting_ocpazure_cost_summary_by_location (usage_start, cluster_id, cluster_alias, resource_location)
            ;

            DROP MATERIALIZED VIEW IF EXISTS reporting_ocpazure_cost_summary_by_service
            ;

            CREATE MATERIALIZED VIEW reporting_ocpazure_cost_summary_by_service AS(
                SELECT row_number() OVER(ORDER BY usage_start, cluster_id, cluster_alias, service_name) as id,
                    usage_start as usage_start,
                    usage_start as usage_end,
                    cluster_id,
                    cluster_alias,
                    service_name,
                    sum(pretax_cost) as pretax_cost,
                    sum(markup_cost) as markup_cost,
                    max(currency) as currency
                FROM reporting_ocpazurecostlineitem_daily_summary
                -- Get data for this month or last month
                WHERE usage_start >= DATE_TRUNC('month', NOW() - '1 month'::interval)::date
                GROUP BY usage_start, cluster_id, cluster_alias, service_name
            )
            ;

            CREATE UNIQUE INDEX ocpazure_cost_summary_service
            ON reporting_ocpazure_cost_summary_by_service (usage_start, cluster_id, cluster_alias, service_name)
            ;

            DROP MATERIALIZED VIEW IF EXISTS reporting_ocpazure_compute_summary
            ;

            CREATE MATERIALIZED VIEW reporting_ocpazure_compute_summary AS(
                SELECT ROW_NUMBER() OVER(ORDER BY usage_start, cluster_id, cluster_alias, instance_type, resource_id) AS id,
                    usage_start,
                    usage_start as usage_end,
                    cluster_id,
                    cluster_alias,
                    instance_type,
                    resource_id,
                    sum(usage_quantity) as usage_quantity,
                    max(unit_of_measure) as unit_of_measure,
                    sum(pretax_cost) as pretax_cost,
                    sum(markup_cost) as markup_cost,
                    max(currency) as currency
                FROM reporting_ocpazurecostlineitem_daily_summary
                WHERE usage_start >= DATE_TRUNC('month', NOW() - '1 month'::interval)::date
                    AND instance_type IS NOT NULL
                GROUP BY usage_start, cluster_id, cluster_alias, instance_type, resource_id
            )
            WITH DATA
            ;

            CREATE UNIQUE INDEX ocpazure_compute_summary
                ON reporting_ocpazure_compute_summary (usage_start, cluster_id, cluster_alias, instance_type, resource_id)
            ;

            DROP MATERIALIZED VIEW IF EXISTS reporting_ocpazure_storage_summary
            ;

            CREATE MATERIALIZED VIEW reporting_ocpazure_storage_summary AS(
                SELECT row_number() OVER(ORDER BY usage_start, cluster_id, cluster_alias, service_name) as id,
                    usage_start as usage_start,
                    usage_start as usage_end,
                    cluster_id,
                    cluster_alias,
                    service_name,
                    sum(usage_quantity) as usage_quantity,
                    max(unit_of_measure) as unit_of_measure,
                    sum(pretax_cost) as pretax_cost,
                    sum(markup_cost) as markup_cost,
                    max(currency) as currency
                FROM reporting_ocpazurecostlineitem_daily_summary
                -- Get data for this month or last month
                WHERE service_name LIKE '%Storage%'
                    AND usage_start >= DATE_TRUNC('month', NOW() - '1 month'::interval)::date
                GROUP BY usage_start, cluster_id, cluster_alias, service_name
            )
            ;

            CREATE UNIQUE INDEX ocpazure_storage_summary
            ON reporting_ocpazure_storage_summary (usage_start, cluster_id, cluster_alias, service_name)
            ;

            DROP MATERIALIZED VIEW IF EXISTS reporting_ocpazure_network_summary
            ;

            CREATE MATERIALIZED VIEW reporting_ocpazure_network_summary AS(
                SELECT row_number() OVER(ORDER BY usage_start, cluster_id, cluster_alias, service_name) as id,
                    usage_start as usage_start,
                    usage_start as usage_end,
                    cluster_id,
                    cluster_alias,
                    service_name,
                    sum(usage_quantity) as usage_quantity,
                    max(unit_of_measure) as unit_of_measure,
                    sum(pretax_cost) as pretax_cost,
                    sum(markup_cost) as markup_cost,
                    max(currency) as currency
                FROM reporting_ocpazurecostlineitem_daily_summary
                -- Get data for this month or last month
                WHERE service_name IN ('Virtual Network','VPN','DNS','Traffic Manager','ExpressRoute','Load Balancer','Application Gateway')
                    AND usage_start >= DATE_TRUNC('month', NOW() - '1 month'::interval)::date
                GROUP BY usage_start, cluster_id, cluster_alias, service_name
            )
            ;

            CREATE UNIQUE INDEX ocpazure_network_summary
            ON reporting_ocpazure_network_summary (usage_start, cluster_id, cluster_alias, service_name)
            ;

            DROP MATERIALIZED VIEW IF EXISTS reporting_ocpazure_database_summary
            ;

            CREATE MATERIALIZED VIEW reporting_ocpazure_database_summary AS(
                SELECT row_number() OVER(ORDER BY usage_start, cluster_id, cluster_alias, service_name) as id,
                    usage_start as usage_start,
                    usage_start as usage_end,
                    cluster_id,
                    cluster_alias,
                    service_name,
                    sum(usage_quantity) as usage_quantity,
                    max(unit_of_measure) as unit_of_measure,
                    sum(pretax_cost) as pretax_cost,
                    sum(markup_cost) as markup_cost,
                    max(currency) as currency
                FROM reporting_ocpazurecostlineitem_daily_summary
                -- Get data for this month or last month
                WHERE service_name IN ('Cosmos DB','Cache for Redis') OR service_name ILIKE '%database%'
                    AND usage_start >= DATE_TRUNC('month', NOW() - '1 month'::interval)::date
                GROUP BY usage_start, cluster_id, cluster_alias, service_name
            )
            ;

            CREATE UNIQUE INDEX ocpazure_database_summary
            ON reporting_ocpazure_database_summary (usage_start, cluster_id, cluster_alias, service_name)
            ;
            """
        ),
    ]
