# Symbolic derivation - [SymPy](https://www.sympy.org/en/index.html)

"SymPy is a Python library for symbolic mathematics. It aims to become a full-featured computer algebra system (CAS) while keeping the code as simple as possible in order to be comprehensible and easily extensible. SymPy is written entirely in Python."

## Symbolically deriving equations of motion

While there is an abundance of physics engines for simulating multibody dynamics ([Mujoco](https://mujoco.org/), [Drake](https://drake.mit.edu/), [Dart](https://dartsim.github.io/), ...) it is still often useful to have analytically derived equations of motion. During your studies you might have come across Lagrangian mechanics, specifically Lagrange's equations of the second kind
$$
\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial \bm{\dot{q}}}\right) - \frac{\partial L}{\partial \bm{q}} = \tau \,,
$$
where $\bm{q}$ are generalized coordinates, $\bm{\tau}$ generalized torques, and $L$ the Lagrangian which is composed of the system's kinetic $T$ and potential $V$ energy:
$$
L = T - V \,.
$$
If you have ever been tasked with derving these equations, even for very simple systems, you know that taking the partial derivates by hand is a time-consuming process with many opportunities to make a mistake. For this reason, today we will derive them using SymPy in a slighly modified form
$$
\underbrace{
\frac{\partial^2 T}{\partial \bm{\dot{q}}^2}
}_{\bm{M}(\bm{q})} \bm{\ddot{q}}
+
\underbrace{
\frac{\partial^2 T}{\partial \bm{\dot{q}} \partial \bm{q}} \bm{\dot{q}} - \frac{\partial T}{\partial \bm{q}}
}_{\bm{c}(\bm{q}, \dot{\bm{q}})}
+
\underbrace{
\frac{\partial V}{\partial \bm{q}}
}_{-\bm{\tau}_p(\bm{q})}
= \bm{\tau} \,,
$$
which also allows us to simply express $\bm{\ddot{q}} = \bm{f}(\dot{\bm{q},\bm{q}}}$.

### Example: cart-pole system

```
                              
                  \
                  /\
                 /  \
                /    \
               l      \
              /       >< m_p
             /       // 
            /       //
          \/       //
           \      //
            \    //
  |   |------\--//------|
  |   |       \//\      |
  g   |  m_c  ( ) theta |
  |   |        |_/      |
  V   |========|========|
_________OOO___|___OOO_________
               |
//|-----s----->|
```

#### Generalized coordinates
$$
\bm{q} = \begin{bmatrix} s \theta \end{bmatrix}^\top \,.
$$

#### Kinetic energy 
$$
T = \frac{1}{2}\left( m_c \, \dot{s}^2 + m_p \, \left( \dot{x}_p^2 + \dot{y}_p^2 \right) \right) \,,
$$
where
$$
\begin{aligned}
	\dot{x}_p &= \dot{s} + l \dot{\theta} \, \cos(\theta) \\
	\dot{y}_p &= l \dot{\theta} \, \sin{\theta} \,. 
\end{aligned}
$$

#### Potential energy
$$
V = g \, m_p \, (1 - l \, \cos(\theta) )
$$ 
