#include <stdio.h>
#include <stdlib.h>

struct node {
	int data;
	struct node* next;
};

void print(struct node* crt){
	while(crt!=NULL){
		printf("%d", crt->data);
		crt=crt->next;
	}
}

struct node* new(int data){
	struct node* snode=NULL;
	snode=(struct node*)malloc(sizeof(struct node));
	snode->data=data;
	snode->next=NULL;
	return snode;
}	

int main(){
	struct node* head=NULL;
	struct node* sec=NULL;
	struct node* thrid=NULL;
	head=(struct node*)malloc(sizeof(struct node));
	sec= (struct node*)malloc(sizeof(struct node));
	thrid=(struct node*)malloc(sizeof(struct node));

	head->data=1;
	head->next=sec;
	sec->data =2;
	sec->next=thrid;
	thrid->data=3;
	thrid->next=new(4);
	print(head);
	return 0;
}

