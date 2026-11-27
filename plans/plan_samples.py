"""Define samples belonging to one experiment and export a typed sample link."""

from datetime import date

from lamindb_setup import evolve as se

from plans.plan_experiments import ExperimentExports, experiments

PLAN_TRANSFORM_STEM_UID = "s7JYZEb8yGuy"


class SampleExports(se.PlanExports):
    sample: se.Feature


@se.create_plan
def samples(
    ctx: se.PlanContext,
    exports: SampleExports,
    experiment_plan: se.Plan[ExperimentExports] = experiments,
) -> None:
    import lamindb as ln

    sample_id = se.Feature("sample_id", dtype=se.LaminDType(str), nullable=False)
    collected_on = se.Feature("collected_on", dtype=se.LaminDType(date), nullable=True)
    schema = se.Schema(
        name="Sample registration",
        features=[sample_id, experiment_plan.exports.experiment, collected_on],
        index=sample_id,
        optionals=[collected_on],
    )
    sheet = se.Sheet("Samples", schema=schema)
    exports.sample = se.Feature(
        "sample", dtype=se.LaminDType(ln.Record, type__uid=sheet.uid), nullable=False
    )
