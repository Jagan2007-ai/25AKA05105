
#include <stdio.h>
#include <stdlib.h>


struct node{
    int data;
    struct node *next;
};


struct node *head= NULL;
struct node*createnode(int val){
    struct node*nn=malloc(sizeof(struct node*));
    nn->data=val;
    nn->next=NULL;
    return nn;
}
int insertion(int val){
    struct node*nn=createnode(val);
    if(head == NULL) {
        head=nn;
    }
    else{
        nn->next=head;
        head=nn;
    }

}
void display(){
    struct node*temp=head;
    while(temp!=NULL){
        printf("%d->",temp->data);
        temp=temp->next;
    }
    printf("NULL\n");
}
int main(){

    insertion(10);
    insertion(20);
    insertion(30);
    insertion(40);
    insertion(50);
    display();
    return 0;

}

























