from cdf.core.insights import Insight, ExpectedTrend
from cdf.query.filter import EqFilter, GtFilter


def get_metadata_insights(metadata):
    """Return the list of insights for a given metadata: title, description or h1
    :param metadata: the input metadata
    :type metadata: str
    :returns: list - the list of corresponding insights_module_name
    """
    result = []

    #unique
    identifier = "meta_{}_unique".format(metadata)
    name = "Unique {}".format(metadata.title())
    field = "metadata.{}.duplicates.nb".format(metadata)
    result.append(
        Insight(
            identifier,
            name,
            ExpectedTrend.UP,
            EqFilter(field, 0)
        )
    )

    #not set
    identifier = "meta_{}_not_set".format(metadata)
    name = "Not Set {}".format(metadata.title())
    field = "metadata.{}.nb".format(metadata)
    result.append(
        Insight(
            identifier,
            name,
            ExpectedTrend.DOWN,
            EqFilter(field, 0)
        )
    )

    #duplicate
    identifier = "meta_{}_duplicate".format(metadata)
    name = "Duplicate {}".format(metadata.title())
    field = "metadata.{}.duplicates.nb".format(metadata)
    result.append(
        Insight(
            identifier,
            name,
            ExpectedTrend.DOWN,
            GtFilter(field, 0)
        )
    )

    return result

#actual insight definition
insights = []
for metadata in ["title", "description", "h1"]:
    insights.extend(get_metadata_insights(metadata))