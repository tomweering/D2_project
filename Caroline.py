# Group meeting demo

#first steps

clear all
close all
clc

# Generate mesh grid

min_x = 0;
min_y = 0;
Lx = 100;
Ly = 100;

x = linspace(min_x, Lx + min_x, 30);
y = linspace(min_y, Ly + min_y, 30);

[X, Y] = meshgrid(x, y);

# show mesh grid

figure()
title('Meshgrid point position')
scatter(X, Y, 'Marker', '.')
axis image

# Generate vectors associated with each point

# Create dummy vector output, to make results repeatable, use a seed
rng('default');
rng(1);
e = rand(size(X));
U = cos(e);
V = sin(e);

figure()
quiver(X, Y, U, V) # quiver plots velocity vectors as arrows with components(u, v) at the points (x, y).
axis image

# Streamslice function

figure()
ss_1 = streamslice(X, Y, U, V, 'noarrows', 'cubic');
title('Using streamslice function at density = 1');

figure()
ss_5 = streamslice(X, Y, U, V, 5, 'noarrows', 'cubic');
title('Using streamslice function at density = 5');

# Streamline generation

U = sin(Y / Ly * pi);
V = cos(X / Lx * 2 * pi);

% % streamline(X, Y, Z, U, V, W, STARTX, STARTY, STARTZ)
creates
streamlines
% from

3
D
vector
data
U, V, W.The
arrays
X, Y, Z
define
the
coordinates
for
    % U, V, W and must
    be
    monotonic and 3
    D
    plaid(as if produced by MESHGRID).
% STARTX, STARTY, and STARTZ
define
the
starting
positions
of
the
stream
% lines.

figure()

% seed
points
to
generate
streamlines
sx = min_x + Lx / 2;
sy = min_y + Ly / 2;

hf = streamline(X, Y, U, V, sx, sy); % this
streamline
goes
along
vector
U, V
from seeding point

(sx, sy)
xlim([min_x, Lx + min_x])
ylim([min_y, Ly + min_y])
axis
image
hold
on
% keyboard
hb = streamline(X, Y, -U, -V, sx, sy); % this
streamline
goes
backward, i.e.vector - U, -V
from seeding point

(sx, sy
 set(hb, 'Color', 'red');

% % how
to
pick
seed
points?

% 1) pick
grid
points

figure()
cla
streamline(X, Y, U, V, X(1: 5:end), Y(1: 5:end)) % forward
hold
on
hb = streamline(X, Y, -U, -V, X(1:5: end), Y(1: 5:end)) % backward
set(hb, 'Color', 'red');

title('1) Seeding points = grid points => density is not homegeneous')

% 2) create
a
finer
grid and then
pick
grid
point?

figure()
cla
streamline(X, Y, U, V, X, Y)
hold
on
hb = streamline(X, Y, -U, -V, X, Y)
set(hb, 'Color', 'red');

title('2) create a finer grid and then pick grid points? => no gain in homogeneity')

% 3) carefully
choose
seed
points
based
on
the
biggest
unfilled
region
% Farthest
point
method
% Mebarki, A., Alliez, P., Devillers, O., 2005.
Farthest
point
seeding
for efficient placement of streamlines, in: VIS
05.
IEEE
Visualization, 2005.
Presented
at
the
VIS
05.
IEEE
Visualization, 2005., pp.
479–486.
https: // doi.org / 10.1109 / VISUAL
.2005
.1532832

% Uses
Delaunay
Triangulation
to
figure
out
the
circumcenter
of
the
largest
% possible
circle.
% more
info: https: // doc.cgal.org / latest / Stream_lines_2 / index.html

                % Create
a
grid
outside
the
domain
bandwidth = 8;

le = -bandwidth + min_x;
re = min_x + Lx + bandwidth;
te = min_y + Ly + bandwidth;
be = min_y - bandwidth;

vx = linspace(le, re, ceil(Lx / bandwidth));
vy = linspace(be, te, ceil(Ly / bandwidth));

[Vx, Vy] = meshgrid(vx, vy);

% frame
only
vv = [Vx(:), Vy(:)];
outer = vv(vv(:, 1) == le | vv(:, 1) == re | ...
vv(:, 2) == be | vv(:, 2) == te,:);


verts = outer;
figure();
axis
square

td = delaunayTriangulation(verts);
triplot(td)
hold
on

[C, r] = circumcenter(td);
mask = C(:, 1) >= min_x & C(:, 1) <= min_x + Lx & ...
C(:, 2) > min_y & C(:, 2) <= min_y + Ly;

C = C(mask,:);
r = r(mask,:);

% find
largest
r
id = find(r == max(r), 1);

% hold
on
startx = round(C(id, 1), 4);
starty = round(C(id, 2), 4);

% draw
a
circle
plot_circ(startx, starty, max(r), 2)
% highlight
centroid
scatter(startx, starty, 100, 'r.')

lines = cell(1);
linenum = 1;

trimdist = bandwidth / 2;

while max(r) >= bandwidth / 2


    figure(10)
    hf = streamline(X, Y, U, V, startx, starty);
    hf.Color = 'r';
    hf.Visible = 'off';
    vvf = [hf.XData' hf.YData'];

    vvf = trim_streamline(verts, ...
    vvf, trimdist);

    hb = streamline(X, Y, -U, -V, startx, starty);
    hb.Visible = 'off';
    vvb = [hb.XData' hb.YData'];

    vvb = trim_streamline(verts, ...
    vvb, trimdist);

    vv = [flipud(vvb);
    ...
    vvf(2: end,:)];

    hold
    on
    plot(vv(:, 1), vv(:, 2), 'b-')

    lines
    {linenum} = vv;
    linenum = linenum + 1;

    verts = [verts;
    vv];

    td = delaunayTriangulation(verts);

    figure(11);
    cla;
    tp = triplot(td);

    [C, r] = circumcenter(td);
    mask = C(:, 1) >= min_x & C(:, 1) <= min_x + Lx & ...
    C(:, 2) > min_y & C(:, 2) <= min_y + Ly & r >= bandwidth / 2;

C = C(mask,:);
r = r(mask,:);

% find
largest
r
id = find(r == max(r), 1);

axis
equal
hold
on
kk = scatter(C(id, 1), C(id, 2), 100, 'Marker', 'o', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'k');

startx = round(C(id, 1), 4);
starty = round(C(id, 2), 4);

% draw
a
circle

plot_circ(startx, starty, max(r), 2)
title(strcat('maximum circle radius =', num2str(max(r))))
drawnow
pause(1)

end

% % Distance
between
curves

% because
of
delaunay
triangulation, distance
between
curves
can
be
% obtained
easily

% get
distance
of
each
line
from neighbors

for i = 1:length(lines)

% make
2
sets - 1
set
with the line itself, and another with every
% other
line
verts1 = vertcat(lines
{1: i - 1});
verts1 = [verts1;
vertcat(lines
{i + 1: length(lines)})];

td = delaunayTriangulation(verts1);
[pl1, d1] = nearestNeighbor(td, lines
{i}(:, 1: 2));

% pop
out
these
closest
points
from verts

verts2 = setdiff(verts1, verts1(pl1,:), 'rows');
td2 = delaunayTriangulation(verts2);
[pl2, d2] = nearestNeighbor(td2, lines
{i}(:, 1: 2));
colrange2 = 10. * d2 / abs(max(d2) - min(d2));

d_average = (d1 + d2) / 2;
colrange = 10 * d_average / abs(max(d2) - min(d2));

figure(12);
axis
equal
ps = plot(verts1(:, 1), verts1(:, 2), 'b.');
hold
on
scatter(lines
{i}(:, 1), lines
{i}(:, 2), [], colrange
');
ps.Visible = 'off';

LAYER.Course(i) = struct('POINT', [lines{i}, d_average]);
end

% % Streamlines and vector
fields in 3
D

close
all

x = 0:10;

[X, Y, Z] = meshgrid(x, x, x);

U = sin(Y / 10 * pi * 2);
V = cos(X / 10 * pi + Z / 10 * pi);
W = ones(size(Z)) * 0.2;

figure()
quiver3(X, Y, Z, U, V, W)
axis
equal

sx = 5;
sy = 5;
sz = 5;

hf = streamline(X, Y, Z, U, V, W, sx, sy, sz);
hb = streamline(X, Y, Z, -U, -V, -W, sx, sy, sz);
hb.Color = 'r';

hb.LineWidth = 3;
hf.LineWidth = 3;

% % delaunay in 3
D

x = X(:);
y = Y(:);
z = Z(:);
T = [x(:) y(:) z(:)];
Tes = delaunayn(T);
figure(2)
tm = tetramesh(Tes, T, 'FaceAlpha', 0.4);

% %
% Functions
needed

function
plot_circ(x, y, r, lw)
t = linspace(0, 2 * pi, 100);
% t = t(1:end - 1);
plot(x + r * cos(t), y + r * sin(t), 'LineWidth', lw);

end

function
trimmed_pts = trim_streamline(all_streamlines, current_streamline, dist_tol)

if isempty(all_streamlines)
trimmed_pts = current_streamline;
else
dists = pdist2(all_streamlines, current_streamline, 'euclidean');
% find
first
instance
of
dists < tol
along
the
current_streamline
aa = dists <= dist_tol;

dist_ind = prod(~aa);

cut_off = find(~dist_ind, 1);

if isempty(cut_off)
trimmed_pts = current_streamline(:,:);
else
trimmed_pts = current_streamline(1:cut_off,:);
end
end

end