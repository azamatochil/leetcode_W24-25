
public class AdjacencyMatrixGraph {
    private boolean adjMatrix[][];
    private int vertexCount;
    public AdjacencyMatrixGraph(int vertexCount) {
        this.vertexCount = vertexCount;
        adjMatrix = new boolean[vertexCount][vertexCount];
    }
}

