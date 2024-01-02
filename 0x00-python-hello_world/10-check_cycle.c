#include "lists.h"

/**
 * check_cycle - a function which checks the linked list
 * @list: The linked list
 * Return: 0 if the linked list doesn't have a cycle, 1 if does
 */
int check_cycle(listint_t *list)
{
listint_t *ptr1 = list->next;
listint_t *ptr2 = list;

while (ptr1 != NULL && ptr1 != ptr2)
{
	ptr1 = ptr1->next;
	ptr2 = ptr2->next;
}
if (ptr1 == NULL)
	return (0);
else
	return (1);
}
