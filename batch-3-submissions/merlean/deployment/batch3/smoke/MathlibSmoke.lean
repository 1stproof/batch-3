import Mathlib.Tactic.Ring
import Lean.Elab.Tactic.Omega
example (a b : Int) : (a+b)^2 = a^2 + 2*a*b + b^2 := by ring
example (n : Nat) : n + 1 > n := by omega
