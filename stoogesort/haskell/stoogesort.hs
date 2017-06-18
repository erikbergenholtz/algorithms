-- stoogesort.hs
-- Avg.:  O(n^(log(3)/log(1.5)))
-- Worst: O(n^(log(3)/log(1.5)))
-- Author: Erik Bergenholtz

import System.IO
import System.Random
import Data.List


swap xs l h = if xs!!l < xs!!h then
                  let first = xs !! l
                      last  = xs !! h
                      left = take l xs
                      middle = take (h-l-1) (drop (l+1) xs)
                      right = drop (h+1) xs
                  in  left ++ [last] ++ middle ++ [first] ++ right
              else xs

stooge xs l h
    | h-l+1 > 2 = stooger (swap xs l h) l h
    | otherwise = swap xs l h

stooger xs l h = stooge (stooge (stooge xs l (h-t)) (l+t) h) l (h-t)
    where t = (h-l+1) `div` 3

randomize :: Int -> StdGen -> [Int]
randomize n = take n . unfoldr (Just . randomR (0,100))

printarr [x] = do
    putStrLn x
printarr (x:xs) = do
    putStrLn x
    print xs

main = do
    seed <- newStdGen
    let rs = randomize 10 seed
    print rs
    print $ stooge rs 0 (length rs - 1)
