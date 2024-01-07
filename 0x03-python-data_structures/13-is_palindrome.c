#include "lists.h"
#include <stdio.h>

/**
 * check_palindrome - checks the plandrome
 * @len: The len of the linked list
 * @arr: The array of the elements
 * Return: 0 or 1
 */
int check_palindrome(size_t len, int *arr);

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
	return (check_palindrome(len, arr));
}

/**
 * check_palindrome - checks the plandrome
 * @len: The len of the linked list
 * @arr: The array of the elements
 * Return: 0 or 1
 */
int check_palindrome(size_t len, int *arr)
{
	size_t i;
	int a, b;

	if (len % 2 == 0)
	{
		for (i = 0; i < len; i++)
		{
			a = arr[i];
			b = arr[(len - 1) - i];
			if (arr[i] != arr[(len - 1) - i])
			{
				free(arr);
				return (0);
			}
		}
	}
	else
	{
		for (i = 0; i < len && i != len / 2; i++)
		{
			if (arr[i] != arr[(len - 1) - i])
			{
				free(arr);
				return (0);
			}
		}
	}
	free(arr);
	return (1);
}
