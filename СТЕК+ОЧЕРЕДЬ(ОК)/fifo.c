#include <stdio.h>
#include <stdlib.h>

int push(int* first,int* last, int* head, int* back, int size, int number);
int pop(int* first,int* last, int* head, int* back, int size);
void print_queue(int* first,int* last, int* head, int* back, int size);

int main(void)
{
    int size;

    printf("Write size: ");
    scanf("%d", &size);

    int* head = malloc(size * sizeof(int));

    if (head == NULL) // проверка на выделение памяти
    {
        printf("Fatal");
        return 1;
    }

    int* back = NULL; // было head;

    // NULL в смысле пусто, тогда можно будет проверять на пустоту
    // когда хранилище опустошится (в ситуации извлечения при head=back), back = NULL

    int* first = head; //указатель на первый элемент массива
    int* last =  head + size; // указатель на последний элемент массива

    printf("head, back : %p %p\n", head, back);
    push(first,last,head,back,size,3);
    printf("head, back : %p %p\n", head, back);

    print_queue(first,last,head,back,size);
    // push(first,last,head,back,size,2);
    // print_queue(first,last,head,back,size);
    // pop(first,last,head,back,size);
    // print_queue(first,last,head,back,size);
    // pop(first,last,head,back,size);
    // print_queue(first,last,head,back,size);
    return 0;
}

int push(int* first,int* last, int* head, int* back, int size, int number)
{
    if (head != last)
    {
        back = head;
        *head = number;
        head = head+1;
        return 1;
    }

    if (head-1 == last && back != first)
    {
        head == first;
        *head = number; 
        printf("add number %d \n", number);
        return 1;
    }
    else
    {
        printf("the queue is full\n");
        return 0;
    }
    return 0;
}

int pop(int* first,int* last, int* head, int* back, int size)
{
    if (back != last)
    {
        back = back + 1;
        printf("pop number\n");
        if (back == head-1)
        {
            back = NULL;
        }
        return 1;
    }
    else
    {
        if (head == first)
        {
            return 0;
        }
        back = first;
        printf("pop number\n");
        if (back == head-1)
        {
            back = NULL;
        }
        return 1;
    }   
}

void print_queue(int* first,int* last, int* head, int* back, int size)
{
    printf("back = %p", back);
    if (back == NULL)
    {
        printf("empty queue\n");
        return;
    }
    printf("%d", *head); 
    //printf("%p %p", head, back);
    if (head != back) 
    {
        int* i = back;
        while (i != head)
        {   
            if(i != last)
            {
                printf("%d\n", *i);
                i+=1; 
                continue;
            }
            if (i == last)
            {
                printf("%d\n", *i);
                i = first;
                continue;
            }
        }
    }
}


int check_full(int* first,int* last, int* head, int* back, int size)
{
    //if(head)
}