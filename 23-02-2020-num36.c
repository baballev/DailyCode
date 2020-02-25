// Given the root of Binary Search Tree, find the second largest node in
// the tree.
// An easy solution to implement consists of in-order traversal it and
// return the node before last, but time + space complexity is O(n) for this
// solution. Here is a O(log(n)) approach.
# include <stdio.h>
# include <stdlib.h>

typedef struct ABR {
  int label;
  struct ABR * left_son;
  struct ABR * right_son;
} ABR;

int second_largest(ABR * root);
// We assume that the BST has at least two elements in it.

int main(int argc, char ** argv){
  // test1
  struct ABR root7 = {7, NULL, NULL};

  struct ABR root8 = {8, &root7, NULL};
  struct ABR root9 = {13, NULL, NULL};
  struct ABR root1 = {23, NULL, NULL};

  struct ABR root5 = {2, NULL, NULL};
  struct ABR root0 = {10, &root8, &root9};
  struct ABR root2 = {25, &root1, NULL};
  struct ABR root3 = {16, NULL, NULL};

  struct ABR root4 = {20, &root3, &root2};
  struct ABR root6 = {5, &root5, &root0};

  struct ABR root = {15, &root6, &root4};

  int i = second_largest(&root);
  printf("Second largest node in the BST: %d\n", i);
}

int second_largest(ABR * root){ // O(log(n))
  struct ABR * next = (ABR*) malloc(sizeof(ABR));
  char is_left_visited = 0;
  if ((*root).right_son) {
    printf("Going Right\n");
    next = (*root).right_son;
  } else {
    printf("Going left\n");
    next = (*root).left_son;
    is_left_visited = 1;
  }
  while (1){
    if ((*next).right_son){
      printf("Going Right\n");
      root = next;
      next = (*next).right_son;
    } else {
      if (is_left_visited) {
        return (*next).label;
      } else {
        if ((*next).left_son){
          printf("Going left\n");
          root = next;
          next = (*next).left_son;
          is_left_visited = 1;
        } else {
          return (*root).label;
        }
      }
    }
  }
}
