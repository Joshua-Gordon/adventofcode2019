import Debug.Trace
import Data.List

split = words . map (\c -> if c == ',' then ' ' else c)

type Wire = [(Int,Int)]

applyInstruction :: Wire -> String -> Wire
applyInstruction w s = let dir = head s
                           len = read $ tail s :: Int
                           (lastx,lasty) = last w
                       in w ++ case dir of
                            'L' -> [(lastx-i,lasty) | i <- [1..len]]
                            'R' -> [(lastx+i,lasty) | i <- [1..len]]
                            'U' -> [(lastx,lasty+i) | i <- [1..len]]
                            'D' -> [(lastx,lasty-i) | i <- [1..len]]

getWire :: Wire -> [String] -> Wire
getWire w (i:is) = getWire (applyInstruction w i) is
getWire w [] = w

intersections :: [Wire] -> [(Int,Int)]
intersections [wa,wb] = intersect wa wb

manhattan (p1,p2) = abs p1 + abs p2

closest :: [(Int,Int)] -> (Int,Int)
closest inters = minimumBy (\p1 p2 -> compare (manhattan p1) (manhattan p2)) [i | i <- inters, i /= (0,0)]

soonest :: [[String]] -> Wire -> Wire -> Int
soonest [i1,i2] w1 w2 = if (not $ null $ intersections [w1,w2]) && (w1 /= [(0,0)] || w2 /= [(0,0)]) then 0 else 1 + soonest [tail i1,tail i2] (traceShowId $ applyInstruction w1 (head i1)) (applyInstruction w2 (head i2))

--main = readFile "input.txt" >>= \f -> print $ closest $ intersections $ traceShowId $ map (getWire [(0,0)] . split) (lines f)

main = readFile "input.txt" >>= \f -> print $ soonest ((map split) $ lines f) [(0,0)] [(0,0)]
