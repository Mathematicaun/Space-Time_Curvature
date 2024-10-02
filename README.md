# 3D Space-Time Curvature Simulation

## Mathematical Explanation

This code simulates the curvature of space-time in a three-dimensional space, utilizing parametric equations based on trigonometric functions. The simulation illustrates how the curvature evolves over time and represents the geometric properties of a 3D surface.

The primary functions used to define the spatial dimensions are:

1. **Length Functions**:
   - The functions `length_x` and `length_y` are defined as follows:
     - $L_x(t_1, o) = -\sqrt{5^2 - t_1^2} + 5 + o$
     - $L_y(t_1, o) = -\sqrt{5^2 - t_1^2} + 5 + o$

   Here, \( o \) serves as an offset that modifies the geometric configuration of the surface, while \( t_1 \) ranges over a specified interval. The square root function provides the boundary condition of the circular geometry defined within a radius of 5 units.

2. **Parametric Equations**:
   The simulation utilizes the following parametric equations to define the surface:
   - $X(j_1, j_2) = \cos(j_1) \cdot L_x(j_2, 3/10 \cdot (t + 5))$
   - $Y(j_1, j_2) = \sin(j_1) \cdot L_y(j_2, 3/10 \cdot (t + 5))$
   - $Z(j_2) = j_2$

   In these equations:
   - \( j_1 \) and \( j_2 \) are parameters derived from a meshgrid that spans the domain of interest.
   - \( t \) represents the time parameter, affecting the curvature over the time evolution of the simulation.

3. **Derivative Approximation**:
   The numerical derivatives are computed to approximate the gradient of the curvature at each point on the surface:
   - $dX(j_1, j_2) = \frac{X(j_1 + do, j_2 + do) - X(j_1, j_2)}{do}$
   - $dY(j_1, j_2) = \frac{Y(j_1 + do, j_2 + do) - Y(j_1, j_2)}{do}$
   - $dZ(j_2) = \frac{Z(j_2 + do) - Z(j_2)}{do}$

   Where \( do = 1 \times 10^{-6} \) is a small increment used for the finite difference approximation.

4. **Magnitude of the Gradient**:
   The magnitude of the gradient is calculated as follows:
   $\text{predicted\_mag} = \sqrt{dX^2 + dY^2 + dZ^2}$

   This magnitude provides insight into the rate of change of the curvature at any given point on the surface. The magnitude is then normalized for color mapping, enhancing visual representation during the animation.

5. **Color Normalization**:
   Color normalization is applied to the quiver arrows representing the directional derivatives. The arrows are colored based on the magnitude of the gradient, facilitating an intuitive understanding of how curvature changes over time.

## Vector Field Representation

The simulation includes quiver plots, which represent the directional derivatives of the space-time curvature. The arrows illustrate the rate and direction of change in the curvature at each point, while the surface is rendered with a semi-transparent color, allowing for a comprehensive visual analysis of the space-time curvature dynamics.

## Usage

To run the simulation, ensure you have the required libraries:

```bash
pip install numpy matplotlib
