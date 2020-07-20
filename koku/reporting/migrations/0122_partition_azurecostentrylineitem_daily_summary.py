# Generated by Django 2.2.13 on 2020-06-17 22:54
import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.indexes
from django.db import migrations
from django.db import models

import reporting.partition.models
from migration_helpers import pg_partition as ppart


# Change reporting_ocpusagelineitem_daily_summary
# to a partitioned table with the same definition
def convert_azurecostentry_lids_to_partitioned(apps, schema_editor):
    # Resolve the current schema name
    target_schema = ppart.resolve_schema(ppart.CURRENT_SCHEMA)
    # This is the table we will model from
    source_table = "reporting_azurecostentrylineitem_daily_summary"
    # This is the target table's name (it will be renamed during the conversion to the source table name)
    target_table = f"p_{source_table}"
    # We'll want a new sequence copied from the original sequence
    new_seq = ppart.SequenceDefinition(
        target_schema,
        f"{target_table}_id_seq",
        copy_sequence={"schema_name": target_schema, "table_name": source_table, "column_name": "id"},
    )
    # We want to change the target tables's 'id' column default
    target_identity_col = ppart.ColumnDefinition(target_schema, target_table, "id", default=ppart.Default(new_seq))
    # We also need to include the identity col as part of the primary key definition
    new_pk = ppart.PKDefinition(f"{target_table}_pkey", ["usage_start", "id"])
    # Init the converter
    p_converter = ppart.ConvertToPartition(
        source_table,
        "usage_start",
        target_table_name=target_table,
        partition_type=ppart.PARTITION_RANGE,
        pk_def=new_pk,
        col_def=[target_identity_col],
        target_schema=target_schema,
        source_schema=target_schema,
    )
    # Push the button, Frank.
    p_converter.convert_to_partition()


class Migration(migrations.Migration):

    dependencies = [("reporting", "0120_partitioned_ocplineitemusage_daily_summary")]

    operations = [
        migrations.AlterModelOptions(name="azurecostentrylineitemdailysummary", options={"managed": False}),
        migrations.RunPython(code=convert_azurecostentry_lids_to_partitioned),
    ]
