#! /usr/bin/env ruby
require 'stackprof'

hexagons  = ((4..12).to_a * 6).map{|n|6*n}
pentagons = ((5..12).to_a * 4).map{|n|5*n}
# all = hexagons + pentagons
all = [24, 24, 24, 24, 25, 25, 30, 30, 30, 30, 30, 30, 30, 35, 35, 36, 40]
c = 0

l = 3

# StackProf.run(mode: :object, raw: true, out: 'counts.dump') do
#   while c< 100
  while true
    s = all.shuffle
    (0...(17-l)).each do |i|
      ((i+l)...17).each do |j|
        strips = s[i..j]
        total = strips.sum
        count = strips.length
        if total % 50 == 0 && total / 50 == count
          puts "i: #{i} j: #{j}\n#{count} strings (#{total} lights)\n#{strips.sort}"
        end

        c+=1
        puts c if c % 10_000_000 == 0
      end
    end
  end
# end
