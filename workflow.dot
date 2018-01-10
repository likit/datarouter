digraph G {
    a [label="edit code"];
    b [label="run tests"];
    c [label="git status"];
    d [label="git diff"];
    e [label="git add"];
    f [label="git commit"];
    g [label="git fetch upstream"];
    h [label="git diff upstream"];
    i [label="pip -r requirements.txt"];
    j [label="git merge upstream"];
    k [label="docker build"];
    l [label="docker run"];
    m [label="docker ps"];
    n [label="docker stop"];
    o [label="git push"];
    p [label="make pull requests"];
    g -> h -> j -> a;
    a -> b -> c -> d -> e -> f;
    a -> i -> b;
    j -> k -> l -> m -> n;
    f -> o;
    o -> a;
    o -> p;
    p -> g;
}