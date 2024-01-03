#include "lists.h"

/**
 * check_cycle - a function which checks the linked list
 * @list: The linked list
 * Return: 0 if the linked list doesn't have a cycle, 1 if does
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
