-- quicksort.hs
-- Avg.   O(n log(n))
-- Worst: O(n^2)
-- Author: Erik Bergenholtz

import System.IO
import System.Random
import Data.List

quicksort :: [Int] -> [Int]
quicksort (x:xs) = (quicksort left) ++ [x] ++ (quicksort right)
    where left = [y | y<-xs, y<=x]
          right = [y | y<-xs, y>x]
quicksort xs = xs

randomize :: Int -> StdGen -> [Int]
randomize n = take n . unfoldr (Just . randomR (0,100))

printarr [x] = do
    putStrLn x
printarr (x:xs) = do
    putStrLn x
    print xs

main = do
    seed <- newStdGen
    let rs = randomize 500 seed
    print $ quicksort rs
