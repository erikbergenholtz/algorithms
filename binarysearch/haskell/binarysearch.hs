-- binarysearch.hs
-- Avg.   O(n log(n))
-- Worst: O(n^2)
-- Author: Erik Bergenholtz
-- Since this algorithm requires the list to be sorted, quicksort is
-- included too

import System.IO
import System.Random
import Data.List

binarysearch x [] _ _ = -1
binarysearch x xs l h
    | l>h = -1
    | xs!!mid == x = mid
    | xs!!mid > x = binarysearch x xs l (mid-1)
    | xs!!mid < x = binarysearch x xs (mid+1) h
    where mid = (div (h+l) 2)

quicksort :: [Int] -> [Int]
quicksort [] = []
quicksort [x] = [x]
quicksort (x:xs) = (quicksort left) ++ [x] ++ (quicksort right)
    where left = [y | y<-xs, y<=x]
          right = [y | y<-xs, y>x]


randomize :: Int -> StdGen -> [Int]
randomize n = take n . unfoldr (Just . randomR (0,100))

main = do
    seed <- newStdGen
    let rs = randomize 50 seed
    print (quicksort rs)
    putStrLn . show $ rs!!0
    putStrLn . show $ binarysearch (rs!!0) ( quicksort rs ) 0 ((length rs)-1)

