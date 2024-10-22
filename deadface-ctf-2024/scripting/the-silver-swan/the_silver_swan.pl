#!/usr/bin/perl

use strict;
use warnings;

{
my $poem = <<'END_POEM';
    The silver Swan, who, living, had no Note,
    when Death approached, unlocked her silent throat.
    Leaning her breast against the reedy shore,
    thus sang her first and last, and sang no more:
    "Farewell, all joys! O Death, come close mine eyes!
     More Geese than Swans now live, more Fools than Wise."
END_POEM

# TODO #1: Define rol, taking a char/8-bit number, and a number of 
#          bits to rotate (0-8), and return the 8-bit number rotated to the
#          left by that many bits.
sub rol {
    my ($num, $rotations) = @_;
    # return [CODE GOES HERE];    
    $rotations %= 8;
    return (($num << $rotations) & 0xFF) | ($num >> (8 - $rotations));
}

# TODO #2: Define ror, taking a char/8-bit number, and a number of 
#          bits to rotate (0-8), and return the 8-bit number rotated to the
#          right by that many bits.
sub ror {
    my ($num, $rotations) = @_;
    # return [CODE GOES HERE];    
    $rotations %= 8;
    return (($num >> $rotations) & 0xFF) | (($num << (8 - $rotations)) & 0xFF);
}

my $encrypt = 0;

my @tokens = [];

# TODO #3: Split $poem string into tokens by spaces, 
#          putting each word into @tokens.
# @tokens = [CODE GOES HERE];
@tokens = split ' ', $poem;

my $m = 'Sewell';

$m =~ s/^..//g;

my $myt1 = my $myt2 = my $myt3 = my $myt4 = '';

foreach my $token (@tokens) {
    # TODO #4: Remove punctuation from the $token string
    # $token = [CODE GOES HERE];
    $token =~ s/[[:punct:]]//g;
    
    # Select the Mighty Ones for AMHO
    $myt1 = $token =~ /$m/     ? $token : $myt1;
    $myt2 = $token =~ /..a.h/  ? $token : $myt2;
    $myt3 = $token =~ /$myt1/  ? $token : $myt3;
    $myt4 = $token =~ /F.{4}/  ? $token : $myt4;
}

my $amho = "${myt1}, ${myt2}; ${myt3}, ${myt4}!";
my $amho_len = length($amho);

#
# TODO #5: Declare an empty dictionary called "amho_bits"
#
# my [CODE GOES HERE];
my %amho_bits;

my $amho_gulja = '';

# Loop through each character in the $amho string
# For each unique character, count the number of "lit" (1) bits in that
#    character.  The result will be a dictionary indexed by the unique
#    characters in $amho, with the value being the number of bits in that
#    ASCII character.

for my $i (0..$amho_len - 1) {
    $amho_gulja = substr($amho, $i, 1);
    # Skip if this character is already in the $amho_bits dictionary
    if (exists($amho_bits{$amho_gulja})) {next};

    $amho_bits{$amho_gulja} = 0;
    my $ascii_value = ord($amho_gulja);

    # Count the number of bits in $amho_gulja and
    # place that value in the $amho_bits dictionary at the
    # key for that character
    for my $j (0..7) {
        my $bit = 0;
    
        # TODO #6: Set $bit to 1 if the current bit of $amho_gulja is lit,
        #       0 if not lit
        # $bit = [CODE GOES HERE];
        $bit = ($ascii_value & (1 << $j)) ? 1 : 0;

        # Add the bit (0 or 1) to the current counter
        $amho_bits{$amho_gulja} += $bit;
    }
}

if ($encrypt) {
    # Read in the binary file "the_silver_swan.txt".
    open my $fh, '<:raw', "the_silver_swan.txt" or die;

    # Encrypt each byte by iterating through the characters of $amho and using
    # the current character as an index into $amho_bits to lookup the number of
    # bits to rotate. To encrypt the byte, rotate the plaintext byte by the 
    # value specified by the key value in $amho_bits TO THE LEFT.  When all of 
    # the bytes of the $amho have been used, return to index 0 and rotate 
    # through the $amho bytes again until the entire plaintext has been
    # encrypted.
    #
    # Write results to STDOUT (captured as "the_silver_swan.enc").
    
    # Each line is 301 characters, ending in 0x0A.
    my $contents = '';
    my $key_idx = 0;
    while(1) {
        my $line = '';
        my $line2 = '';
        my $success = read $fh, $line, 301, length($line);
        die $! if not defined $success;
        last if not $success;
        for my $i (0..length($line) - 1) {
            # Get a byte
            my $dec_char = ord(substr($line, $i, 1));
            
            # Get how many bits to rotate it
            my $rotate_bits = $amho_bits{substr($amho, $key_idx % length($amho), 1)};
            
            # TODO #7: Rotate $dec_char by $rotate_bits to get $enc_char
            # my $enc_char = [CODE GOES HERE];
            my $enc_char = rol($dec_char, $rotate_bits);
            
            # Add encrypted character to the line
            $line2 .= chr($enc_char);

            # Increment the key index
            $key_idx++;
        }
        # Add the line to the contents.
        
        $contents .= $line2; 
    }
    print $contents;
    
} else { # Decrypting
    # Decrypt each byte by iterating through the characters of $amho and using
    # the current character as an index into $amho_bits to lookup the number of \
    # bits to rotate. To encrypt the byte, rotate the plaintext byte by the 
    # value specified by the key value in $amho_bits TO THE RIGHT.  When all of 
    # the bytes of the $amho have been used, return to index 0 and rotate 
    # through the $amho bytes again until the entire plaintext has been
    # decrypted.
    #
    # Write results to STDOUT (captured as "the_silver_swan.dec").
    
    # Read in the binary file "the_silver_swan.dec".
    open my $fh, '<:raw', "the_silver_swan.enc" or die;
    
    # Each line is 301 characters, ending in 0x0A.
    my $contents = '';
    my $key_idx = 0;
    while(1) {
        my $line = '';
        my $line2 = '';
        my $success = read $fh, $line, 301, length($line);
        die $! if not defined $success;
        last if not $success;
        #for my $i (0..length($line)) {
        foreach(split(//, $line)){
            # Get a byte
            my $enc_char = ord($_);
            
            # Get how many bits to rotate it            
            my $rotate_bits = $amho_bits{substr($amho, $key_idx % length($amho), 1)};
            
            # TODO #8: Rotate $enc_char by $rotate_bits to get $dec_char
            # my $dec_char = [CODE GOES HERE];   
            my $dec_char = ror($enc_char, $rotate_bits);         
            
            # Add the decrypted character to the line
            $line2 .= chr($dec_char);

            # Increment the key index
            $key_idx++;
        }
        
        # Add the line to the contents.
        $contents .= $line2; 
    }
    print $contents;    
}

}

