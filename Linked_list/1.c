#include <stdio.h>
#include <stdlib.h>
typedef struct node{
    char a;
    struct node *next;
};

int len_list(node *head);
void rotate_left(node **head, int i);
int main(void) {
    int i;
	node *root;
	root = (node *)malloc(sizeof(node));
	node *head = root;
	for(i=0;i<10;i++){
    	root->next = (node *)malloc(sizeof(node));
    	root->a = 0x30+i;
    	if(i+1>=10) root->next = NULL;
    	root = root->next;
	}

	rotate_left(&head,4);
	root = head;
    while(root){
        printf("%c ",root->a);
    	root = root->next;
	}
	return 0;
}
int len_list(node *head){
    
    int i = 0;
    node *root = head;
    while(root) {
        i+=1;
        root = root->next;
    }
    return i;
    
}
void rotate_left(node **head,int i){
    node *root = *head;
    node *temp = *head;
    node *temp1 = *head;
    int l  = i;
    while(l--)root = root->next;
    //printf("%c\n",root->a);
    *head = root;
    while(temp1->next)temp1 = temp1->next;
    //printf("%c\n",temp1->a);
    temp1->next = temp;
    while(temp->next != *head)temp = temp->next;
    //printf("%c\n",temp->a);
    temp->next = NULL;
    
}
