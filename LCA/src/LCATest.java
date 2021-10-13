import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import static org.junit.Assert.assertEquals;

@RunWith(JUnit4.class)
public class LCATest {
    //LCA lca = new LCA();
    // Creating nodes for testing

    /* Arranging these nodes into the following tree:
                A
               / \
              B   C
            /  \   \
           D   E    F
              /
            G
    */
    @Test
    public void testNode() {
        Node A = new Node();
        Node B = new Node();
        Node C = new Node();
        A.setLeft(B);
        A.setRight(C);
        assertEquals("Checking setLeft", B, A.getLeft());
        assertEquals("Checking setRight", C, A.getRight());
    }

    @Test
    public void testLCA() {
        Node A = new Node();
        Node B = new Node();
        Node C = new Node();
        Node D = new Node();
        Node E = new Node();
        Node F = new Node();
        Node G = new Node();
        A.setLeft(B);
        A.setRight(C);
        B.setLeft(D);
        B.setRight(E);
        C.setRight(F);
        E.setLeft(G);

        assertEquals("Checking LCA of root + root", A, LCA.lowestCommonAncestor(A, A, A));
        assertEquals("Checking LCA of B + C", A, LCA.lowestCommonAncestor(B, C, A));
        assertEquals("Checking LCA of D + F", A, LCA.lowestCommonAncestor(D, F, A));
        assertEquals("Checking LCA of D + E", B, LCA.lowestCommonAncestor(D, E, A));
    }
}
