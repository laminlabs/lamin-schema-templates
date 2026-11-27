"""Define the experiment register and the link other plans can reuse."""

from lamindb_setup import evolve as se

PLAN_TRANSFORM_STEM_UID = "5NK2FJnZm25k"


class ExperimentExports(se.PlanExports):
    experiment: se.Feature


@se.create_plan
def experiments(ctx: se.PlanContext, exports: ExperimentExports) -> None:
    import lamindb as ln

    experiment_id = se.Feature(
        "experiment_id", dtype=se.LaminDType(str), nullable=False
    )
    title = se.Feature("experiment_title", dtype=se.LaminDType(str), nullable=True)
    schema = se.Schema(
        name="Experiment registration",
        features=[experiment_id, title],
        index=experiment_id,
        optionals=[title],
    )
    sheet = se.Sheet("Experiments", schema=schema)
    exports.experiment = se.Feature(
        "experiment",
        dtype=se.LaminDType(ln.Record, type__uid=sheet.uid),
        nullable=False,
    )
