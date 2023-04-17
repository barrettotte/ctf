// https://lib.rs/install/libbruteforce

// use libbruteforce::hash_fncs::sha256_hashing;
use libbruteforce::hash_fncs::md5_hashing;
use libbruteforce::BasicCrackParameter;
use libbruteforce::{symbols, CrackParameter, TargetHashInput};
use simple_logger::SimpleLogger;

fn main() {
    SimpleLogger::new().with_utc_timestamps().init().unwrap();

    let alphabet = symbols::Builder::new()
        // .with_lc_letters()
        // .with_common_special_chars()
        // .with_char('a')
        // .with_char('b')
        // .with_char('c')
        // .with_char('d')
        .with_char('☊')
        .with_char('☋')
        .with_char('☌')
        .with_char('☍')
        .build();

    // sha256("a+c")
    // let sha256_hash = "3d7edde33628331676b39e19a3f2bdb3c583960ad8d865351a32e2ace7d8e02d";

    
    // let md5_hash = "900150983cd24fb0d6963f7d28e17f72"; // md5("abc")
    // let md5_hash = "6f18c394574309bf65f78e41cb08a43b"; // md5("aadbacabadda")
    let md5_hash = "3bc33aacbcae59c2707b61da18a25d2a";

    // let len = 128;
    let len = 20;

    // the actual cracking
    let res = libbruteforce::crack(CrackParameter::new(
        BasicCrackParameter::new(alphabet, len, len, true),
        md5_hashing(TargetHashInput::HashAsStr(md5_hash)),
    ));

    if let Some(solution) = res.solution() {
        println!("Password is: {}", solution);
        println!("Took {:.3}s", res.duration_in_seconds());
    } else {
        println!("Did not find password!");
        std::process::exit(1);
    }
}
