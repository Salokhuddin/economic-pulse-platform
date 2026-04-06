from core.models.raw import RawFredSeries


def load_fred_series(series_id, validated_data):
    """Load validated FRED observations into the raw_fred_series table."""
    fred_series_model = []
    for observation in validated_data["observations"]:
        row = RawFredSeries(
            series_id=series_id,
            units=validated_data["units"],
            date=observation["date"],
            value=observation["value"],
        )
        fred_series_model.append(row)
    RawFredSeries.objects.bulk_create(fred_series_model, ignore_conflicts=True)
