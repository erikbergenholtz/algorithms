/*
 * mergesort.c
 * Avg.:  O(n log(n))
 * Worst: O(n log(n))
 * Author: Erik Bergenholtz
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 100

void merge(int *, size_t, int *, size_t, int *);
int *mergesort(int *, size_t);
void print(int *, size_t);

int main(int argc, char ** argv)
{
	srand(time(NULL));
	int arr[N];
	for(size_t i=0 ; i<N ; ++i)
		arr[i] = rand()%100;
	print(arr, N);
	int *merged = mergesort(arr, N);
	print(merged,N);
	free(merged);
	return 0;
}

void merge(int *l, size_t nL, int *r, size_t nR, int* merged)
{
	size_t iL=0;
	size_t iR=0;
	size_t i=0;
	while( iL < nL && iR < nR)
	{
		if(l[iL] >= r[iR])
			merged[i++] = l[iL++];
		else
			merged[i++] = r[iR++];
	}
	while(iL < nL)
		merged[i++] = l[iL++];
	while(iR < nR)
		merged[i++] = r[iR++];
}

int *mergesort(int *arr, size_t n)
{
	if(n <= 1)
		return arr;
	size_t nL = n/2;
	size_t nR = n-nL;
	int *l = mergesort(arr,nL);
	int *r = mergesort(&arr[nL],nR);
	int *merged = (int*)malloc(sizeof(int)*(nL+nR));
	merge(l,nL,r,nR, merged);
	if(nL > 1)
		free(l);
	if(nR > 1)
		free(r);
	return merged;
}

void print(int *arr, size_t n)
{
	for(size_t i=0 ; i<n ; ++i)
	{
		printf("%d ",arr[i]);
	}
	printf("\n");
}
