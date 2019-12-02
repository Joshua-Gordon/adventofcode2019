{-main = do
    f <- readFile "input.txt"
    print $ sum $ map (\l -> (l `div` 3) - 2) $ map read $ lines f
    -}

--part 2
getFuel l = if l < 9 then 0 else ((l `div` 3) - 2) + getFuel ((l `div` 3) - 2)
main = readFile "input.txt" >>= \f -> print $ sum . (map getFuel) . (map read) . lines $ f
