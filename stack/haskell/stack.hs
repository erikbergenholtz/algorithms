-- stack.hs
-- Author: Erik Bergenholtz

type Stack a = [a]

push :: a -> Stack a -> Stack a
push x xs = x:xs

pop :: Stack a -> (Maybe a, Stack a)
pop [] = (Nothing,[])
pop (x:xs) = (Just x, xs)

peek :: Stack a -> Maybe a
peek [] = Nothing
peek (x:xs) = Just x

peekAt :: Int -> Stack a -> Maybe a
peekAt i xs
    | i >= length xs = Nothing
    | otherwise = Just (xs!!i)
