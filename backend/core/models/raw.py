from django.db import models


class RawFredSeries(models.Model):
    """Raw FRED API observations, stored as-is for reprocessing."""

    series_id = models.CharField(max_length=50)
    date = models.DateField()
    value = models.DecimalField(max_digits=25, decimal_places=10, null=True)
    units = models.CharField(max_length=20)
    ingested_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "raw_fred_series"
        constraints = [
            models.UniqueConstraint(
                fields=["series_id", "date"],
                name="unique_series_date",
            )
        ]
