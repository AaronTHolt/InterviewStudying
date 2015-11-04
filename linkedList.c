#include <stdio.h>
#include <stdlib.h>

struct node {
	int x;
	struct node *next;
};

void appendNode(struct node *curr, int data)
{
	//While there is no empty space
	while (curr->next != 0)
	{
		curr = curr->next;
	}

	//allocate space for new node
	curr->next = malloc(sizeof(struct node));

	//move pointer to new node
	curr = curr->next;

	//set latest node attributes
	curr->x = data;
	curr->next = 0;
}

void printLinkList(struct node *curr)
{
	//While there is no empty space
	while (curr->next != 0)
	{
		if (curr->x != NULL)
		{
			printf("%d ", curr->x);
		}
		curr = curr->next;
	}
	//Catch last one, add newline
	printf("%d\n", curr->x);
}

void insertNode(struct node *curr, int data)
{
	//Save pointer to next node
	struct node *temp;
	temp = curr->next;

	//allocate space for new node
	curr->next = malloc(sizeof(struct node));

	//move pointer to new node
	curr = curr->next;

	//set latest node attributes
	curr->x = data;
	curr->next = temp;
}

//Delete one node with data if it exists
//Pass in ROOT node only
int deleteNode(struct node *curr, int data)
{

	//check if data is at root
	//Don't delete root just set data to null
	if (curr->x == data)
	{
		curr->x = NULL;
		return 1;
	}


	struct node *previous, *next;
	previous = curr;
	//While there is no empty space
	while (curr->next != 0)
	{
		if (curr->x == data)
		{
			break;
		}
		else
		{
			//save previous pointer
			previous = curr;
			curr = curr->next;
		}
	}

	if (curr->next == 0){
		if (curr->x != data)
		{
			return 0;
		}
		else
		{
			previous->next = 0;
			free(curr);
		}
	}
	else
	{
		//save next link, delete
		next = curr->next;
		free(curr);
		previous->next = next;
	}
}

int main()
{
	//declare root node
	struct node *root;
	root = (struct node *) malloc(sizeof(struct node));

	//Next doesn't exist yet, set to null
	root->next = 0;

	//Root data
	root->x = 42;


	appendNode(root, 46);
	appendNode(root, 46);
	printLinkList(root);
	insertNode(root, 22);
	printLinkList(root);
	deleteNode(root, 46);
	printLinkList(root);
	deleteNode(root, 46);
	printLinkList(root);
	deleteNode(root, 42);
	printLinkList(root);
}
