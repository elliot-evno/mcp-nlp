from fastmcp import FastMCP

from app.services.text_distance import TextDistanceEvaluator

textdistance_mcp = FastMCP("MCP: Text Distance Calculator")


@textdistance_mcp.tool()
async def measure(
    source: str,
    reference: str,
    algorithm: str = "levenshtein",
    metric: str = "normalized_similarity",
) -> float:
    """Measures text distance between two sequences of strings using various algorithms."""

    evaluator = TextDistanceEvaluator(algorithm=algorithm, metric=metric)
    return evaluator.compute(source, reference)
