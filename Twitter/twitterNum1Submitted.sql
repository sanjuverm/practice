/*
Enter your query here.
*/
/*SELECT * from tree; /*the first column is ID and second is P_ID*/
/*
Naive Code and Logic (# indicates my logic procession)
SELECT Id, #print the node id column
CASE WHEN #create a new column for type values
P_id IS NULL #if there is no parent id, the node is a root 
THEN "Root" #name it root
WHEN
Id IN (SELECT P_Id FROM Tree) #if the node id is also a parent id, it is Inner
THEN "Inner" #name it Inner 
ELSE "Leaf" #anything else (specifically, nodes that aren't in the parent id column at all) is a leaf
END AS Type #name column Type
FROM Tree #get the data from the Tree Table
ORDER BY Id; #order by node id

*/


SELECT
  DISTINCT (node.Id),
  CASE
    WHEN (parent_node.Id IS NULL) AND (child_node.P_id IS NOT NULL) THEN "Root"
    WHEN (child_node.Id IS NULL) AND (parent_node.Id IS NOT NULL) THEN "Leaf"
    ELSE "Inner"
  END AS node_type

FROM
    Tree node
    LEFT Join Tree parent_node
        ON node.P_Id = parent_node.Id
    LEFT Join Tree child_node
        ON node.Id = child_node.P_id
ORDER BY
    node.Id;