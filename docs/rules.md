# Rules

SlopGuard provides a suite of rules specifically tuned for code generated rapidly without sufficient architectural thought.

## List of Rules
- **useless_wrapper_function**: Detects functions that just forward arguments to another function without adding any behavior.
- **abstraction_inflation**: Detects over-splitting of basic operations into trivial classes or functions.
- **duplicate_helper_pattern**: Detects newly created helper functions that are near-clones of existing helpers.
- **dead_code_signals**: Detects unreachable branches, stale unused imports, and empty pass statements.
- **broad_exception**: Detects `except Exception:` swallows inside internal components.
- **fake_edge_case_handling**: Detects branches handling conditions that could never structurally occur.
- **no_op_indirection**: Detects pass-through classes.
- **style_drift**: Compares changes to repo baseline parameters like function lengths and comment densities.
