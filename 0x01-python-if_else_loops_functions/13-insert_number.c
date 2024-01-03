#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node in the linked list
 * @head: The head of the linked list
 * @number: The number inside the cell
 * Return:Null if failed, the address of the new node if success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	return (new_node);
}
