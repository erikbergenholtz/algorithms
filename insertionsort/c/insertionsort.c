/*
 * insertionsort.c
 * O(n^2)
 */

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define MAX 100
#define LEN 100

void randomize(int *, size_t);
void swap(int *, int *);
void insertionSort(int *, size_t);
void print(int *, size_t);

int main( void )
{
	srand(time(NULL));
	int arr[LEN];
	randomize(arr, LEN);
	insertionSort(arr, LEN);
	print(arr, LEN);
	return 0;
}

void randomize(int *arr, size_t l)
{
	for(size_t i=0 ; i<l ; ++i)
	{
		arr[i] = rand()%MAX;
	}
}

void swap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void insertionSort(int *arr, size_t l)
{
	for(size_t i=0 ; i<l ; ++i)
	{
		int index=i;
		for(size_t j=i+1 ; j<l ; ++j)
		{
			if(arr[index]>arr[j]) index=j;
		}
		if(index != i) swap(&arr[i], &arr[index]);
	}
}

void print(int *arr, size_t l)
{
	for(size_t i=0 ; i<l ; ++i)
	{
		printf("%d\n",arr[i]);
	}
}
