from .utils import _import_string

__all__ = ["TextDistanceEvaluator"]


class TextDistanceEvaluator:
    """
    Measures text distance between two strings using various algorithms.
    """

    def __init__(
        self,
        algorithm: str,
        metric: str = "normalized_similarity",
    ):
        try:
            # Use import_module for importing "textdistance" package and target algorithm
            self.algorithm = _import_string(f"textdistance.{algorithm}")
        except ImportError as e:
            raise ValueError(f"Unsupported algorithm: '{algorithm}'") from e
        self.metric = metric

    def compute(self, source: str, reference: str) -> float:
        """
        Calculates text distance between source and reference segments.
        """
        try:
            return getattr(self.algorithm, self.metric)(source, reference)
        except AttributeError as e:
            raise ValueError(f"Unsupported metric: '{self.metric}'") from e
