function convertTermsToJson(inputText) {
    // Handle empty or invalid input
    if (!inputText || typeof inputText !== 'string') {
        throw new Error('Input must be a non-empty string');
    }

    // Split the input text into lines and filter out empty lines
    const lines = inputText.split('\n').filter(line => line.trim());

    // Process each line and create term-definition pairs
    const terms = lines.map(line => {
        // Split on <ans> delimiter
        const [term, definition] = line.split('<ans>');

        // Validate that we have both term and definition
        if (!term || !definition) {
            throw new Error(`Invalid format in line: ${line}`);
        }

        return {
            term: term.trim(),
            definition: definition.trim()
        };
    });

    // Create the final JSON structure
    return {
        terms: terms  // Changed from 'flashcards' to 'terms' to match existing format
    };
}
