# Home Page Flow Diagram

```mermaid
graph TD
    A[Show auctions] --> B{Get all active auctions}
    B -->|Success| C[Display auctions]
    C --> D[Display auction details]
    D --> E[Get bid amount]
    E --> F{Validate bid amount}
    F -->|Invalid| G[Display error message]
    F -->|Valid| H{Check auction status}
    H -->|Auction ended| I[Display error message]
    H -->|Auction active| J{Check if user is seller}
    J -->|User is seller| K[Display error message]
    J -->|User is not seller| L{Place bid}
    L -->|Success| M[Display success message]
    G --> C
    I --> D
    K --> D
    M --> C
```
