-- mergesort.hs
-- Avg.   O(n log(n))
-- Worst: O(n log(n))
-- Author: Erik Bergenholtz

import System.IO
import System.Random
import Data.List

merge :: Ord a => [a] -> [a] -> [a]
merge [] [] = []
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys)
    | x>=y = x:(merge xs (y:ys))
    | otherwise = y:(merge (x:xs) ys)

mergesort :: Ord a => [a] -> [a]
mergesort [] = []
mergesort [x] = [x]
mergesort xs = merge (mergesort left) (mergesort right)
    where left = take ( length xs `div` 2 ) xs
          right = drop ( length xs `div` 2) xs

randomize :: Int -> StdGen -> [Int]
randomize n = take n . unfoldr (Just . randomR (0,100))

printarr [x] = do
    putStrLn x
printarr (x:xs) = do
    putStrLn x
    print xs

main = do
    seed <- newStdGen
    let rs = randomize 50 seed
    print $ mergesort rs
