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
	int list_len, act_len, i;
	listint_t *first = *head;
	listint_t *second = NULL;
	listint_t *prev = NULL;
	listint_t *temp = NULL;
	
	if (head == NULL || *head == NULL)
		return (1);
	
	list_len = list_length(head);
	act_len = (list_len % 2 == 0) ? (list_len / 2) : (list_len / 2) + 1;
	
	for (i = 0; i < act_len; i++)
	{
		temp = first;
		while (temp->next != NULL)
		{
			prev = temp;
			temp = temp->next;
		}
		second = temp;
		if (first->n != second->n)
			return (0);
		prev->next = NULL;
		free(second);
		first = first->next;
	}
	return (1);
}

