#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * list_length - a function that returns the length of a list
 * @head: the list head address
 * Return: length of the list
 */

int list_length(listint_t **head)
{
	int len = 0;
	listint_t *list_cpy = *head;

	if (head == NULL || *head == NULL)
		return (0);
	while (list_cpy != NULL)
	{
		len += 1;
		list_cpy = list_cpy->next;
	}
	return (len);
}

/**
 * is_palindrome - a function to check if the list is a pallindrome
 * @head: list address
 * Return: 0 if not palindrome, 1 otherwise
 */

int is_palindrome(listint_t **head)
{
	int list_len, act_len, i, j;
	listint_t *first = NULL;
	listint_t *second = NULL;

	if (head == NULL || *head == NULL)
		return (1);
	printf("Test one\n\n");
	first = malloc(sizeof(listint_t));
	if (first == NULL)
		return (0);
	second = malloc(sizeof(listint_t));
	if (second == NULL)
	{
		free(first);
		return (0);
	}
	printf("Test two\n\n");
	first = *head;
	second = *head;
	list_len = list_length(head);
	act_len = (list_len % 2 == 0) ? (list_len / 2) :
		(list_len / 2) - 1;
	printf("Test three\n\n");
	for (i = 1; i <= act_len; i++)
	{
		for (j = list_len; j >= i; j--)
		{
			second = second->next;
			printf("Test tfor incrementing second\n\n");
		}
		if (first->n != second->n)
		{
			printf("Test for not pallindrome\n\n");
			free(first);
			free(second);
			return (0);
		}
		printf("Test for not pallindrome\n\n");
		first = first->next;
		second = second->next;
	}
	printf("Test successful execution\n\n");
	return (1);
}
