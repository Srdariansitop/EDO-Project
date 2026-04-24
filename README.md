# EDO-Project

Academic project for the numerical solution of **Ordinary Differential Equations (ODE)** of first order using advanced numerical methods.

## Description

This project implements an **ODE solver** that allows solving ordinary differential equations of the form:

```
dy/dx = f(x, y)
```

Using the **Runge-Kutta 4th order method** and provides an interactive graphical interface to visualize results.

## User Interface

![EDO-Project Interface](Image/X2.jpg)

The graphical interface allows you to enter parameters intuitively and immediately visualizes:
- The numerical solution obtained
- The direction field (isoclines)
- The approximation points of the Runge-Kutta method

## Project Structure

```
EDO-Project/
├── main.py              # Main graphical interface (Tkinter)
├── numerica.py          # Numerica Class: Numerical operations and Runge-Kutta 4
├── Function.py          # Function Class: Evaluation of mathematical functions
├── Interpolation.py     # Interpolation Class: Newton-Gregory Method
├── grafico.py           # Function for plotting direction fields
├── tests.py             # Unit tests
└── Image/               # Graphics resources folder
```

## Components

### 1. **Function.py** 
Parses and evaluates mathematical expressions in string:
- Supports: `sin`, `cos`, `exp`, `log`, `e`, basic operations
- Converts notation (e.g., `^` to `**`)

### 2. **numerica.py** 
Implements numerical operations:
- **Runge-Kutta 4** method for solving ODE
- Machine epsilon calculation
- Absolute and relative error analysis

### 3. **Interpolation.py** 
**Newton-Gregory** method with divided differences:
- Constructs interpolating polynomials of degree n
- Calculates divided differences table
- Useful for approximating solutions at intermediate points

### 4. **grafico.py** 
Visualization:
- Direction field (isoclines)
- Solution curve with Runge-Kutta points
- matplotlib support

### 5. **main.py** 
Complete graphical interface with:
- ODE input in format `dy/dx`
- Initial parameters (x₀, y₀, step h, final x)
- Integrated graph visualization

## Usage Examples

### Via Graphical Interface (main.py)
```bash
python main.py
```
1. Enter the differential equation: `x + y`
2. Define initial conditions (x₀, y₀)
3. Specify step (h) and final point (xf)
4. Visualize the solution and direction field

### Via Code
```python
from numerica import Numerica
from Function import Function

f = Function("x + y")  # dy/dx = x + y
numerica = Numerica()

# Solve with Runge-Kutta 4
result = numerica.runge_kutta_4(
    f, 
    x0=0, y0=1,    # Initial conditions
    h=0.1,         # Step
    xi=1           # Final point
)

print(result)  # [(x0,y0), (x1,y1), ..., (xf,yf)]
```

## Tests

Run unit tests:
```bash
python tests.py
```

Tests include:
- Linear functions: `x + y`
- Exponential functions: `y`
- Trigonometric functions: `cos(x) + sin(y)`

## Numerical Methods and Concepts

### Runge-Kutta 4th Order

The fourth-order Runge-Kutta method is an explicit numerical scheme widely used for the approximate solution of initial value problems in ordinary differential equations. This method belongs to the family of one-step Runge-Kutta methods and is characterized by its excellent relationship between computational precision and computational cost.

#### Mathematical Formulation

Given a differential equation of the form:
$$\frac{dy}{dx} = f(x, y)$$

with initial condition $y(x_0) = y_0$, the 4th order Runge-Kutta method approximates the solution by:

$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

Where the coefficients $k_i$ are calculated as:
- $k_1 = f(x_n, y_n)$ - Slope at the beginning of the interval
- $k_2 = f(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1)$ - Slope at the midpoint using $k_1$
- $k_3 = f(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_2)$ - Slope at the midpoint using $k_2$
- $k_4 = f(x_n + h, y_n + hk_3)$ - Slope at the end of the interval

#### Interpretation

This method performs four evaluations of the function $f$ in each step. The weighted combination $(k_1 + 2k_2 + 2k_3 + k_4)/6$ represents a weighted average of the slopes, where greater importance is given to the evaluations at the midpoint of the interval. This strategy better captures the behavior of the solution within the interval $[x_n, x_{n+1}]$.

#### Convergence Properties

- **Global convergence order**: 4 (global error of $O(h^4)$)
- **Local convergence order**: 5 (local error of $O(h^5)$)
- **Stability**: It is stable for a wide range of problems, although it has limitations with stiff problems
- **Computational complexity**: Requires 4 evaluations of $f$ per step

#### Advantages and Limitations

**Advantages:**
- High precision with a moderate number of function evaluations
- Stable for most non-stiff problems
- Excellent precision/computational cost ratio
- Widely implemented and well documented

**Limitations:**
- Not suitable for stiff problems (where there are very different time scales)
- Requires the function to be sufficiently smooth
- The step size $h$ must be small enough to ensure convergence

### Newton-Gregory Interpolation

#### Introduction

The Newton-Gregory interpolation method is a technique that constructs a polynomial that passes exactly through a given set of points. This polynomial is called an **interpolating polynomial** and can be used to:
- Estimate intermediate values not directly calculated
- Approximate complex functions using polynomials
- Obtain information about the behavior of the solution between calculation points

#### Mathematical Formulation

Given a set of points $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$, the method constructs a polynomial of degree $n$ using **divided differences**.

This technique iteratively calculates a divided differences table:

$$f[x_0] = f(x_0)$$
$$f[x_0, x_1] = \frac{f(x_1) - f(x_0)}{x_1 - x_0}$$
$$f[x_0, x_1, x_2] = \frac{f[x_1, x_2] - f[x_0, x_1]}{x_2 - x_0}$$

And so on until the complete table is obtained.

The Newton interpolating polynomial is expressed as:

$$P(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + ... + f[x_0, ..., x_n](x - x_0)...(x - x_{n-1})$$

#### Advantages of the Method

1. **Computational efficiency**: Does not require solving systems of linear equations
2. **Flexibility**: Allows adding new points without recalculating everything from scratch
3. **Numerical stability**: Better conditioning than other methods such as Lagrange
4. **Compact representation**: The polynomial is expressed hierarchically

#### Application in the Project

In this project, Newton-Gregory interpolation is used to:
- Obtain approximations of behavior between points calculated by Runge-Kutta
- Validate the smoothness of the numerical solution
- Allow evaluations at intermediate points without recalculating

### Machine Epsilon

#### Concept

The **machine epsilon** is the smallest difference that a computer can represent between 1.0 and the next representable real number in its floating-point system. It represents the level of relative precision in numerical calculations.

#### Mathematical Meaning

In Python, it uses the IEEE 754 double precision standard (64 bits). The machine epsilon for this format is approximately:

$$\epsilon \approx 2.22 \times 10^{-16}$$

This means that any number that differs from the exact result by less than $\epsilon$ times the number will be considered equal to that number on the computer.

#### Importance in Numerical Methods

1. **Precision limit**: No matter how many iterations we perform, we can never achieve more precision than $\epsilon \times |y|$ in the result
2. **Convergence criteria**: A stopping criterion should be established that is reasonably greater than $\epsilon$
3. **Error analysis**: Provides a theoretical lower bound for numerical error

#### Calculation in the Project

In the `Numerica` class, you can obtain the machine epsilon with:

```python
epsilon = Numerica.obtener_epsilon()
print(epsilon)  # ≈ 2.220446049250313e-16
```

#### Practical Implications

- **Repeated operations**: Rounding errors accumulate with each operation
- **Catastrophic cancellation**: Subtracting very close numbers can cause loss of significant digits
- **Result validation**: An error less than $\epsilon$ is practically "non-existent" in machine terms

### Calculation of Absolute and Relative Error

#### Absolute Error

The **absolute error** is the difference between the approximate value (obtained numerically) and the exact value (or reference):

$$E_a = |y_{exact} - y_{approx}|$$

Where:
- $y_{exact}$: Theoretical value or reference solution
- $y_{approx}$: Value obtained by the numerical method (Runge-Kutta in this case)

**Characteristics**:
- It is expressed in the same units as the variable
- Provides a direct measure of deviation
- Does not allow comparing errors between problems with different scales

**Example**: If the exact solution is $y = 3.142$ and you obtain $y = 3.141$, then $E_a = 0.001$

#### Relative Error

The **relative error** normalizes the absolute error with respect to the exact value, allowing precision comparison independently of scale:

$$E_r = \frac{|y_{exact} - y_{approx}|}{|y_{exact}|} \times 100\%$$

Or in decimal form (without percentage):

$$E_r = \frac{|y_{exact} - y_{approx}|}{|y_{exact}|}$$

**Characteristics**:
- It is expressed as a percentage (when multiplied by 100)
- It is dimensionless (without units)
- Allows comparing the quality of approximations at different scales

**Example**: If $y_{exact} = 3.142$ and $y_{approx} = 3.141$, then $E_r = \frac{0.001}{3.142} \times 100\% \approx 0.032\%$

#### Implementation in the Project

In the `Numerica` class, the `calcular_error` method performs these calculations:

```python
def calcular_error(self, valor_real, texto_respuesta):
    """
    Calculates absolute and relative error.
    
    Args:
        valor_real: Known exact value
        texto_respuesta: Approximate result in format 'y = value'
    
    Returns:
        tuple: (absolute_error, relative_error_percentage)
    """
    y_aprox = float(texto_respuesta.split("y = ")[1])
    error_absoluto = abs(valor_real - y_aprox)
    error_relativo = (error_absoluto / abs(valor_real)) * 100
    return error_absoluto, error_relativo
```

#### Result Interpretation

| Relative Error | Interpretation |
|---|---|
| < 0.001% | Excellent precision |
| 0.001% - 0.1% | Very good precision |
| 0.1% - 1% | Good precision |
| 1% - 5% | Acceptable precision |
| > 5% | Requires method or parameter revision |

#### Relationship with Runge-Kutta 4

Common errors in Runge-Kutta 4:
- **Local truncation error**: $O(h^5)$ at each step
- **Global accumulated error**: $O(h^4)$ after multiple steps
- **Rounding error**: Grows proportionally to the number of steps $N = (x_f - x_0)/h$

Reducing $h$ decreases truncation error but increases the number of operations and, consequently, rounding error.

## User Input Parameters

The graphical interface requests the following parameters to solve the differential equation:

### 1. Differential Equation (dy/dx)

**Description**: The ordinary differential equation you wish to solve, expressed as $\frac{dy}{dx} = f(x, y)$.

**Format**: Enter only the right side of the equation (the function $f(x, y)$).

**Valid examples**:
- `x + y` for $\frac{dy}{dx} = x + y$
- `x*y` for $\frac{dy}{dx} = xy$
- `sin(x) + y` for $\frac{dy}{dx} = \sin(x) + y$
- `exp(-x)*y` for $\frac{dy}{dx} = e^{-x}y$
- `y**2 - x` for $\frac{dy}{dx} = y^2 - x$

**Supported functions**: `sin`, `cos`, `exp`, `log`, `e` (Euler's constant)

### 2. Initial Condition: $x_0$ (Xo)

**Description**: The initial value of the independent variable $x$ from which numerical integration begins.

**Meaning**: It is the starting point of the domain. For example, if you are modeling a physical process that begins at time $t=0$, then $x_0 = 0$.

**Example**: If you enter `0`, the method will start from the point $(0, y_0)$.

**Range**: Generally a real number, although it depends on the context of the problem.

### 3. Initial Condition: $y_0$ (Yo)

**Description**: The initial value of the dependent variable $y$ at the point $x_0$.

**Meaning**: It is the value of the solution that is known at the initial point. Together with $x_0$, it completely specifies the initial condition that guarantees a unique solution.

**Example**: If the problem is $\frac{dy}{dx} = x + y$ with $y(0) = 1$, then enter $y_0 = 1$.

**Importance**: Small variations in $y_0$ can produce significantly different solutions, especially in nonlinear differential equations.

### 4. Step Size: $h$

**Description**: The increment of the independent variable in each iteration of the Runge-Kutta method.

**Meaning**: The domain is discretized into intervals of length $h$. The method calculates approximations at the points $x_0, x_0 + h, x_0 + 2h, ..., x_f$.

**Impact on precision**:
- $h$ small $\Rightarrow$ Greater precision but more computation time
- $h$ large $\Rightarrow$ Lower precision but faster computation

**Recommendations**:
- For typical problems: $0.01 \leq h \leq 0.1$
- For greater precision: $h \leq 0.01$
- For problems with rapid variations: $h \leq 0.001$

**Example**: With $h = 0.1$ and integrating from $x_0 = 0$ to $x_f = 1$, approximations will be calculated at: $0, 0.1, 0.2, ..., 1.0$ (11 points).

**Local error**: The local truncation error is of the order $O(h^5)$ for Runge-Kutta 4.

### 5. Final Point: $x_f$ (Xi)

**Description**: The final value of the independent variable $x$ where you wish to stop integration.

**Meaning**: Defines the solution interval $[x_0, x_f]$. The method will integrate from $x_0$ to $x_f$ in steps of size $h$.

**Example**: If you enter $x_f = 5$, starting from $x_0 = 0$ with $h = 0.1$, you will obtain 51 solution points.

**Relationship with number of steps**: 
$$N = \frac{x_f - x_0}{h}$$

**Considerations**:
- Larger intervals can reveal long-term behavior of the solution
- But they also increase cumulative error (global error)
- Must be greater than $x_0$: $x_f > x_0$

## Requirements

- Python 3.8+
- `tkinter` (included in Python)
- `numpy`
- `matplotlib`
- `sympy`
- `Pillow` (PIL)

### Installing dependencies:
```bash
pip install numpy matplotlib sympy pillow
```


## Notes

- The step `h` should be small for greater precision
- Ill-conditioned functions may require smaller steps
- Interpolation is useful for estimating intermediate values
- Always consider machine epsilon when setting convergence criteria
- Compare absolute and relative error to evaluate solution quality

---


