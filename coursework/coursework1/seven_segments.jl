function seven_segment(pattern::Array{Int64})
    function to_bool(a::Int64)
        return a==1
    end    
    function vert(d1,d2,d3)
        println(
            (d1 ? "|" : " ")*
            (d3 ? "_" : " ")*
            (d2 ? "|" : " "))
    end
    pattern_b=map(to_bool,pattern)
    println(pattern_b[1] ? " _ " : "   ")
    vert(pattern_b[2],pattern_b[3],pattern_b[4])
    vert(pattern_b[5],pattern_b[6],pattern_b[7])
    number=0
    for i in 0:3
        if pattern_b[7+i+1]
            number+=2^i
        end
    end
    println(number)
end

hexdigits = Matrix{Int8}([
    0 0 1 0 0 1 0 1 0 0 0 
    1 0 1 1 1 0 1 0 1 0 0 
    1 0 1 1 0 1 1 1 1 0 0 
    0 1 1 1 0 1 0 0 0 1 0 
    1 1 0 1 0 1 1 1 0 1 0 
    1 1 0 1 1 1 1 0 1 1 0 
    1 0 1 0 0 1 0 1 1 1 0 
    1 1 1 1 1 1 1 0 0 0 1 
    1 1 1 1 0 1 1 1 0 0 1 
    1 1 1 1 1 1 0 0 1 0 1 
    0 1 0 1 1 1 1 1 1 0 1 
    1 1 0 0 1 0 1 0 0 1 1 
    0 0 1 1 1 1 1 1 0 1 1 
    1 1 0 1 1 0 1 0 1 1 1 
    1 1 0 1 1 0 0 1 1 1 1
    1 1 1 0 1 1 1 0 0 0 0 ]) .* 2 .- 1;
one , two, three, four  = [ hexdigits[i,:] for i in  1:4 ];
five, six, seven, eight = [ hexdigits[i,:] for i in  5:8 ];
nine, hexA, hexB, hexC  = [ hexdigits[i,:] for i in  9:12];
hexD, hexE, hexF, zero  = [ hexdigits[i,:] for i in 13:16];

test1 = Int64[1,-1,1,1,-1,1,1,-1,-1,-1,-1]
test2 = Int64[1,1,1,1,1,1,1,-1,-1,-1,-1]

if abspath(PROGRAM_FILE) == @__FILE__
    seven_segment(three)
    seven_segment(six)
    seven_segment(one)
    println("test1")
    seven_segment(test1)
    println("test2")
    seven_segment(test2)
end