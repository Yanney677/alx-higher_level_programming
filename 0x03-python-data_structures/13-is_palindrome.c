#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list to reverse
 *
 * Return: pointer to the head of the reversed list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current_node)
	{
		next = current_node->next;
		current_node->next = prev;
		prev = current_node;
		current_node = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the of the linked list
 *
 * Return: 1 if it is, otherwise 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *small = *head, *big = *head, *tmp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		big = big->next->next;
		if (!big)
		{
			dup = small->next;
			break;
		}
		if (!big->next)
		{
			dup = small->next->next;
			break;
		}
		small = small->next;
	}

	reverse_listint(&dup);

	while (dup && tmp)
	{
		if (tmp->n == dup->n)
		{
			dup = dup->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
