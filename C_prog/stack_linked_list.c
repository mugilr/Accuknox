#include <stdio.h>
#include <stdlib.h>
 
struct node {
    int data;
    struct node* next;
};
 
struct node* new(int data)
{
    struct node* node = (struct node*)malloc(sizeof(struct node));
    node->data = data;
    node->next = NULL;
    return node;
}
 
int isEmpty(struct node* root)
{
    return !root;
}
 
void push(struct node** root, int data)
{
    struct node* node = new(data);
    node->next = *root;
    *root = node;
    printf("%d pushed\n", data);
}
 
int pop(struct node** root)
{
    if (isEmpty(*root))
        return -1;
    struct node* temp = *root;
    *root = (*root)->next;
    int popped = temp->data;
    free(temp);
 
    return popped;
}
 
int top(struct node* root)
{
    if (isEmpty(root))
        return -1;
    return root->data;
}
 
int main()
{
    struct node* root = NULL;
 
    push(&root, 1);
    push(&root, 2);
   // push(&root, 3);
 
    printf("%d popped\n", pop(&root));
    printf("%d popped\n", pop(&root)); 
    printf("Top element: %d\n", top(root));
 
    return 0;
}
