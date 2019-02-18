#! /usr/bin/env ruby

all = (0...100).to_a
l = 40
(0...(100-l)).each do |x|
  ((x+l)...100).each do |y|
    puts "l: #{all[x..y].length}" if all[x..y].length < l
  end
end
