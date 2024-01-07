#include "lists.h"
/**
 * is_palindrome - a function to check if the linked list is palindrome
 * @head: The head, AKA the start of the linked list
 * Return: 0 if not, 1 if yes
 */
int is_palindrome(listint_t **head)
{
	size_t len = 0, i;
	listint_t *node = *head;
	int *arr;

	while (node != NULL)
	{
		len++;
		node = node->next;
	}
	if (len == 0)
		return (0);

	arr = malloc(sizeof(int) * len);
	i = 0;

	node = *head;
	while (node != NULL)
	{
		arr[i] = node->n;
		i++;
		node = node->next;
	}

	if (len % 2 == 0)
	{
		for (i = 0; i < len; i++)
		{
			if (arr[i] != arr[len - i])
				return (1);
		}
	}
	else
	{
		for (i = 0; i < len && i != (len / 2 + 1); i++)
		{
			if (arr[i] != arr[len - i])
				return (1);
		}
	}

	return (0);
}
