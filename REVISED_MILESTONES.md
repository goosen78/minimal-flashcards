# Milestones for Flashcarding App

## Before giving the assignment

We can show a demo of the minimal flashcarding app and briefly describe what is going on. Then we can show a more fleshed out version and explain what has been done to bring it to that stage. After which we can release the assignment along with the milestones proposed below.

## Milestone 1: Environment Setup, Codebase Understanding, CI/CD, and Testing

Duration : `1 week`

Since this is the first milestone we can have the following subtasks:

### 1. Setup Claude Code on your computer

**Tasks**:
- Install Claude Code CLI tool following the official documentation
- Configure Claude Code with your API credentials
- Familiarize yourself with basic Claude Code commands
- Test Claude Code by asking it to explain a simple file in the repository

**Deliverable**: Create a short tutorial (written guide or video, 3-5 minutes) showing:
- Installation steps for your operating system
- Basic configuration
- Example usage (e.g., asking Claude to explain code, generate tests, etc.)

### 2. GitHub Repository Setup

**Tasks**:
- Create a GitHub account (if you don't have one)
- Fork or clone the `minimal-flashcards` repository
- Set up SSH keys for GitHub authentication (recommended)
- Create a development branch for your work
- Make your first commit (e.g., add a README update with your name)
- Push your changes to GitHub

**Success Criteria**:
- GitHub repository is accessible and properly configured
- Can push and pull changes successfully
- Understand basic Git workflow (branch, commit, push, pull)

### 3. Understand the Codebase

**Tasks**:

**Tech Stack Analysis**:
- Identify frontend technologies (React, TypeScript, Vite, etc.)
- Identify backend technologies (FastAPI, SQLModel, PostgreSQL, etc.)
- Document the development tools used (testing frameworks, linters, etc.)
- Create a simple architecture diagram showing how components interact

**Backend Endpoints**:
- Start the backend server locally
- Access the API documentation at `http://localhost:8000/docs`
- Document all available endpoints by category:
  - Authentication endpoints (signup, login, logout, etc.)
  - Deck management endpoints (create, read, update, delete)
  - Card management endpoints
  - Study session endpoints
- Test at least 3 endpoints using the Swagger UI or curl/Postman

**Frontend Functionalities**:
- Start the frontend development server
- Document the available pages/routes:
  - Landing page
  - Login/Signup pages
  - Dashboard
  - Deck detail page
  - Study session page
- Map each frontend page to the backend endpoints it uses
- Identify the state management approach (Zustand, React Query)

**Test Cases Analysis**:
- Locate test files in both `backend/tests/` and `frontend/src/` (if any)
- Run existing tests (backend: `pytest`, frontend: `npm test`)
- Document what each test file tests:
  - Unit tests vs integration tests
  - What functionality is covered
  - What functionality is NOT covered
- Identify gaps in test coverage

**Deliverable**: Create a comprehensive codebase analysis document covering:
- Tech stack overview
- Complete list of backend endpoints with descriptions
- Frontend page/route inventory with functionality descriptions
- Test coverage summary
- Architecture diagram (can be hand-drawn or using a tool)

### 4. Implement a CI Pipeline for the Project

**Goal**: Set up continuous integration using GitHub Actions to automatically run tests on every push and pull request.

**Tasks**:

1. Create `.github/workflows/ci.yml` file with the following jobs:

   **Backend Tests Job**:
   - Set up Python 3.11 environment
   - Start PostgreSQL service (use GitHub Actions services)
   - Install backend dependencies
   - Run Alembic migrations
   - Run pytest with coverage
   - Upload coverage report

   **Frontend Tests Job**:
   - Set up Node.js 18 environment
   - Install frontend dependencies
   - Run frontend tests (if any exist)
   - Run build to ensure no compilation errors

   **Linting Job** (optional but recommended):
   - Backend: Run Black or Ruff for code formatting checks
   - Frontend: Run ESLint and Prettier checks

2. Test the CI pipeline:
   - Make a small change and push to GitHub
   - Verify that the workflow runs automatically
   - Check that all jobs complete successfully
   - Fix any failures

3. Add status badge to README.md showing build status

**Success Criteria**:
- CI pipeline runs automatically on push and pull requests
- All tests pass in the CI environment
- Build completes successfully
- Status badge visible in README

**Deliverable**: Create a short explanation/demo video (3-5 minutes) showing:
- The CI configuration file and what each part does
- A live demonstration of pushing code and seeing CI run
- How to view CI results and debug failures
- Best practices for using CI in development

### 5. Write Test Cases Using Claude

**Goal**: Demonstrate proficiency with testing frameworks and Claude Code by writing comprehensive test cases.

**Backend Tests** (minimum 5 test cases):

Write tests for at least one of these areas:
- **Authentication tests**: Test signup, login, logout, token refresh
- **Deck CRUD tests**: Test creating, reading, updating, deleting decks
- **Card operations tests**: Test adding cards to decks, updating cards
- **Study session tests**: Test creating sessions, submitting answers
- **Data validation tests**: Test invalid inputs, edge cases

Example test structure:
```python
# tests/test_decks.py
def test_create_deck_success(client, test_user_token):
    """Test creating a deck with valid data"""
    # Test implementation

def test_create_deck_unauthorized(client):
    """Test that creating a deck without auth fails"""
    # Test implementation
```

**Frontend Tests** (minimum 5 test cases):

Write tests for at least one of these areas:
- **Component tests**: Test that components render correctly
- **User interaction tests**: Test button clicks, form submissions
- **Store tests**: Test Zustand auth store functionality
- **API integration tests**: Test API calls with mocked responses
- **Route protection tests**: Test that protected routes redirect when not authenticated

Example test structure:
```typescript
// components/__tests__/DeckCard.test.tsx
describe('DeckCard', () => {
  it('renders deck name and card count', () => {
    // Test implementation
  });

  it('navigates to deck detail on click', () => {
    // Test implementation
  });
});
```

**Using Claude Code**:
- Use Claude to help generate test cases
- Ask Claude to explain testing best practices
- Have Claude suggest edge cases to test
- Use Claude to help debug failing tests

**Success Criteria**:
- At least 5 backend tests written and passing
- At least 5 frontend tests written and passing
- Tests cover both happy paths and error cases
- Tests are well-documented with clear descriptions
- All tests pass locally and in CI

**Deliverable**:
- Test files committed to repository
- Brief document explaining:
  - What each test covers and why it's important
  - How you used Claude Code to assist in writing tests
  - Any challenges faced and how you overcame them

## Milestone 2

Duration : `1 week`

This milestone contains 3 streams. A student can pick 2 out of the three and implement them. The three streams are:
1. native CSS to Tailwind CSS framework migration
2. Implement complex question types like `MCQs`, `Short answers`, and `Cloze`
3. Spaced repetition algorithm for basic type cards

### Stream 1 : Native CSS to Tailwind CSS migration

**Goal**: Modernize the application's styling framework by migrating from native CSS to Tailwind CSS for better maintainability and consistency.

**Tasks**:
1. Install and configure Tailwind CSS in the frontend project
   - Install dependencies: `npm install -D tailwindcss postcss autoprefixer`
   - Initialize configuration files (`tailwind.config.ts`, `postcss.config.js`)
   - Update `index.css` with Tailwind directives
2. Migrate existing CSS styles to Tailwind utility classes
   - Convert landing page styles
   - Convert dashboard and deck detail page styles
   - Convert study session page styles
   - Replace custom CSS classes with Tailwind utilities
3. Create reusable component patterns using Tailwind
   - Button variants (primary, secondary, danger)
   - Card components
   - Form inputs and labels
4. Ensure responsive design is maintained or improved
5. Test all pages to verify visual consistency

**Success Criteria**:
- All custom CSS removed (except Tailwind configuration)
- Consistent design language across all pages
- Responsive layouts work on mobile, tablet, and desktop
- Build process successfully compiles Tailwind CSS

### Stream 2 : Implement complex question types

**Goal**: Extend the flashcard system beyond basic Q&A to support Multiple Choice Questions (MCQs), Short Answer questions, and Cloze deletion cards.

**Tasks**:

**Backend**:
1. Update the `Card` model to support different card types
   - Add `card_type` field (enum: basic, multiple_choice, short_answer, cloze)
   - Add `options_json` field for storing MCQ options and other type-specific data
2. Create or update database migration using Alembic
3. Update card validation schemas to handle type-specific data
4. Implement business logic for each card type in the service layer

**Frontend**:
1. Create card type-specific components:
   - `MultipleChoiceCard.tsx` - Display 4 options (A, B, C, D), handle selection, show correct answer
   - `ShortAnswerCard.tsx` - Text input for user answer, display expected answer on reveal
   - `ClozeCard.tsx` - Parse `{{c1::hidden text}}` syntax, show blanks initially, reveal on flip
2. Update `StudySessionPage.tsx` to render the appropriate card component based on type
3. Update deck creation/editing UI to allow users to:
   - Select card type when creating cards
   - Provide type-specific information (options for MCQ, expected answers for short answer, etc.)
4. Add visual indicators for card types in deck detail view

**Success Criteria**:
- Database supports all four card types
- Users can create cards of each type through the UI
- Study sessions correctly render and handle interaction for each card type
- MCQ cards validate correct answer selection
- Short answer cards display expected answers
- Cloze cards properly parse and display blanks

### Stream 3 : Spaced repetition algorithm

**Goal**: Implement the SM-2 spaced repetition algorithm to optimize long-term learning and retention.

**Tasks**:

**Backend**:
1. Verify or create `SRSReview` model with fields:
   - `repetitions` (number of times reviewed)
   - `interval_days` (days until next review)
   - `easiness` (easiness factor)
   - `due_at` (next review date)
   - `last_quality` (quality of last response, 0-5)
2. Implement SM-2 algorithm logic in `services/study.py`:
   - Quality < 3: Reset card (repetitions=0, interval=1)
   - Quality >= 3: Increase interval based on repetitions and easiness
   - Update easiness factor based on quality rating
   - Calculate next due date
3. Create API endpoint `GET /reviews/due` to fetch cards due for review
4. Update study session answer submission to trigger SM-2 calculations
5. Implement streak tracking (consecutive days studied)

**Frontend**:
1. Add "Review" study mode with quality rating buttons (1-5)
   - 1: Complete blackout
   - 2: Incorrect, but familiar
   - 3: Correct with difficulty
   - 4: Correct with hesitation
   - 5: Perfect recall
2. Display review queue count on dashboard ("X cards due today")
3. Show next review date for each card in deck detail page
4. Add study statistics and visualizations:
   - Current streak counter
   - Study heatmap (calendar view showing daily activity)
   - Progress indicators (new/learning/review counts per deck)
5. Create dedicated review mode that only shows due cards

**Success Criteria**:
- SM-2 algorithm correctly calculates review intervals based on quality ratings
- Cards rated < 3 reset to the beginning of the learning cycle
- Dashboard accurately displays count of due cards
- Review mode only shows cards that are due or overdue
- Streak counter increments on consecutive study days
- Study heatmap visualizes user activity over time
- Next review dates are visible for all studied cards



## Milestone 3: AI Integration for Flashcard Generation

Duration : `1 week`

**Goal**: Integrate Large Language Models (LLMs) into the application to automatically generate flashcards from text input or document uploads. Support both cloud-based models (ChatGPT/OpenAI, Claude/Anthropic) and locally hosted models (Ollama).

### Tasks

### Phase 1: LLM Service Setup and Configuration

**Backend Setup**:
1. Install required dependencies:
   ```bash
   pip install openai anthropic ollama PyPDF2 python-pptx python-docx
   ```

2. Create `services/llm_service.py` with provider abstraction:
   - Implement `generate_with_openai(prompt, model)` for OpenAI GPT models
   - Implement `generate_with_anthropic(prompt, model)` for Claude models (optional)
   - Implement `generate_with_ollama(prompt, model)` for local Ollama models
   - Create unified interface `generate_flashcards(text, question_types, count, provider)`

3. Configure environment variables:
   - Add `OPENAI_API_KEY` for OpenAI integration
   - Add `ANTHROPIC_API_KEY` for Claude integration (optional)
   - Add `OLLAMA_BASE_URL` (default: `http://localhost:11434`)
   - Add `DEFAULT_LLM_PROVIDER` setting

4. Implement provider selection logic:
   - Try local Ollama first (cost-effective)
   - Fallback to cloud API if local unavailable
   - Allow user override of provider preference

### Phase 2: Document Parsing

**Backend**:
1. Create `services/file_parser.py` with parsing functions:
   - `parse_pdf(file)` - Extract text from PDF files using PyPDF2
   - `parse_pptx(file)` - Extract text from PowerPoint files using python-pptx
   - `parse_docx(file)` - Extract text from Word documents using python-docx
   - `parse_txt(file)` - Read plain text files

2. Implement robust error handling:
   - Handle corrupted or password-protected files
   - Handle unsupported file formats gracefully
   - Limit file size (e.g., max 10MB)
   - Validate file types before parsing

3. Add file upload validation and sanitization

### Phase 3: AI Flashcard Generation Logic

**Backend**:
1. Create endpoint `POST /api/v1/ai/generate` that accepts:
   - Text input (raw text pasted by user) OR file upload
   - Question types to generate (basic, multiple_choice, short_answer, cloze)
   - Number of cards to generate
   - LLM provider preference (optional)
   - Deck name for generated cards

2. Design prompts for each card type:

   **Basic Q&A**:
   - Prompt: "Generate simple question-answer flashcards from this text..."
   - Expected output: JSON array with `question` and `answer` fields

   **Multiple Choice**:
   - Prompt: "Generate multiple choice questions with 4 options..."
   - Expected output: JSON with `question`, `options` (array of 4), `correct_answer_index`

   **Short Answer**:
   - Prompt: "Generate short answer questions..."
   - Expected output: JSON with `question`, `expected_answers` (array of acceptable answers)

   **Cloze Deletion**:
   - Prompt: "Generate cloze deletion cards using {{c1::text}} syntax..."
   - Expected output: JSON with `text` containing cloze markers

3. Implement LLM response parsing:
   - Parse JSON responses from LLM
   - Validate that responses match expected schema
   - Handle malformed responses with retry logic
   - Sanitize generated content

4. Create deck and cards in database:
   - Generate deck with AI-generated flag
   - Create cards with appropriate types
   - Associate cards with deck
   - Return deck ID and summary

5. Add error handling for LLM failures:
   - API rate limits
   - Timeout errors
   - Invalid responses
   - Quota exceeded errors

### Phase 4: Frontend Integration

**Frontend**:
1. Create `AIPoweredDecksPage.tsx` with the following sections:

   **Text Input Section**:
   - Large textarea for pasting text content
   - Character counter (e.g., "500 / 5000 characters")
   - Sample text button to demonstrate functionality

   **File Upload Section**:
   - File input supporting PDF, PPTX, DOCX, TXT
   - Drag-and-drop zone
   - File preview showing name and size
   - Clear uploaded file button

   **Configuration Section**:
   - Deck name input field
   - Question type checkboxes:
     - [ ] Basic Q&A
     - [ ] Multiple Choice
     - [ ] Short Answer
     - [ ] Cloze Deletion (if Stream 2 implemented)
   - Number of cards slider (5-50 cards)
   - LLM provider selector (dropdown):
     - Auto (tries local first, then cloud)
     - Ollama (local)
     - OpenAI GPT-4
     - Claude (if implemented)

   **Generation Section**:
   - "Generate Flashcards" button
   - Loading state with progress indicator
   - Status messages ("Parsing document...", "Generating cards...", "Creating deck...")

2. Create `components/GeneratedCardPreview.tsx`:
   - Display generated cards before saving
   - Allow editing of individual cards
   - Allow deleting unwanted cards
   - Show card type indicators

3. Implement generation workflow:
   - Validate inputs (text or file required, at least one question type selected)
   - Upload file or send text to backend
   - Show loading state during generation
   - Display preview of generated cards
   - Allow user to review and edit
   - Save deck to database on confirmation
   - Navigate to deck detail page after saving

4. Add error handling:
   - Display user-friendly error messages
   - Handle file upload failures
   - Handle LLM API errors
   - Provide retry option

### Phase 5: AI Answer Checking (Optional Stretch Goal)

If you implemented Stream 2 (complex question types), add AI-powered answer checking for short answer questions:

1. Create endpoint `POST /api/v1/ai/check-answer`:
   - Accept user's answer and expected answer(s)
   - Use LLM to semantically compare answers
   - Return correctness score (0-100) and feedback

2. Integrate into study session:
   - When user submits short answer, send to AI for checking
   - Display AI feedback (e.g., "Correct! Your answer captures the main idea.")
   - Allow manual override (user can mark as correct/incorrect)

### Success Criteria

**Backend**:
- [ ] LLM service successfully integrates with at least one provider (Ollama or OpenAI)
- [ ] Can parse PDF, PPTX, and DOCX files correctly
- [ ] Endpoint generates flashcards from text input
- [ ] Generated cards are saved to database with correct types
- [ ] Error handling works for common failure scenarios
- [ ] API is documented in Swagger UI

**Frontend**:
- [ ] AI-powered decks page is accessible from dashboard
- [ ] Can input text or upload file
- [ ] Can configure question types and card count
- [ ] Generation process shows clear loading states
- [ ] Preview shows generated cards before saving
- [ ] Can edit or delete individual generated cards
- [ ] Successfully creates deck and navigates to it

**Integration**:
- [ ] If Ollama is running locally, it is used by default
- [ ] If Ollama is unavailable, falls back to cloud API
- [ ] Generated decks include metadata (AI-generated flag, source text preview)
- [ ] If Stream 2 implemented, can generate all card types (basic, MCQ, short answer, cloze)

**Testing**:
- [ ] Test with various input sources (copied text, PDF, PPTX)
- [ ] Test generation with different LLM providers
- [ ] Test error scenarios (invalid file, API failure, etc.)
- [ ] Write at least 3 backend tests for AI generation endpoint
- [ ] Write at least 2 frontend tests for AI decks page

### Deliverables

1. **Code**: Fully functional AI integration committed to repository
2. **Documentation**:
   - README section explaining how to set up Ollama (if using)
   - Environment variable documentation for API keys
   - Usage guide showing how to generate AI flashcards
3. **Demo**: Short video or written guide demonstrating:
   - Uploading a document and generating flashcards
   - Reviewing and editing generated cards
   - Studying the AI-generated deck

### Optional Enhancements

If you finish early, consider adding:
- **Batch generation**: Generate multiple decks from multiple files
- **Template customization**: Allow users to customize generation prompts
- **Source tracking**: Link each card back to specific page/section of source document
- **Smart chunking**: Automatically split large documents into manageable sections
- **Cost tracking**: Display estimated API costs for cloud LLM usage

## Extra Credit: Comprehensive Implementation + Exam Mode

**Prerequisites**: Complete all three streams from Milestone 2:
- Stream 1: Tailwind CSS migration
- Stream 2: Complex question types (MCQ, Short Answer, Cloze)
- Stream 3: Spaced repetition algorithm

**Goal**: Implement a comprehensive Exam Mode that filters for complex question types, enforces strict completion rules, includes a countdown timer, and uses AI to evaluate short answer responses.

### Requirements

### 1. Exam Mode Backend

**Database Schema Updates**:
1. Extend `QuizSession` model to support exam mode:
   - Add `study_mode` field with new value: `exam`
   - Add `time_limit_seconds` field (optional, for timed exams)
   - Add `exam_config` JSON field to store:
     - Included card types
     - Shuffle settings
     - Time limit
     - Passing score threshold

2. Extend `QuizResponse` model:
   - Add `time_spent_seconds` field (time spent on individual card)
   - Add `ai_feedback` field (for AI-evaluated short answers)
   - Add `ai_score` field (0-100, for short answers)

**API Endpoints**:
1. `POST /api/v1/study/sessions/exam` - Create exam session:
   - Filter cards by type (exclude basic type)
   - Accept configuration:
     - `deck_id` (required)
     - `time_limit_minutes` (optional, default: 30)
     - `shuffle` (boolean, default: true)
     - `passing_score` (optional, default: 70)
   - Return session with filtered cards

2. `POST /api/v1/study/sessions/{session_id}/submit` - Submit exam:
   - Accept all answers at once (array of responses)
   - For MCQs: Auto-grade based on correct answer
   - For short answers: Send to AI for evaluation
   - For cloze: Compare user input to expected text
   - Calculate final score
   - Mark session as completed
   - Return detailed results

3. `GET /api/v1/study/sessions/{session_id}/results` - Get exam results:
   - Return summary:
     - Total score (percentage)
     - Time taken
     - Number correct/incorrect per question type
     - Pass/fail status
     - Per-question breakdown with feedback

**AI Answer Evaluation Service**:
1. Extend `services/llm_service.py`:
   - Add `evaluate_short_answer(user_answer, expected_answer, question)`:
     - Use LLM to semantically compare answers
     - Return score (0-100) and detailed feedback
     - Handle edge cases (empty answers, off-topic responses)

2. Batch evaluation for efficiency:
   - Group short answer questions together
   - Send to LLM in one request (faster, cheaper)
   - Parse individual results from batch response

### 2. Exam Mode Frontend

**Create `ExamSessionPage.tsx`**:

**Pre-Exam Screen**:
1. Display exam configuration:
   - Deck name
   - Number of questions (by type)
   - Time limit (if set)
   - Passing score threshold
2. Show instructions:
   - "You must answer all questions before submitting"
   - "Basic flashcards are excluded from exam mode"
   - "Short answers will be evaluated by AI"
   - "You cannot pause or exit during the exam"
3. "Start Exam" button

**During Exam**:
1. **Timer Component** (if time limit set):
   - Countdown timer displayed at top
   - Warning color when < 5 minutes remaining
   - Auto-submit when time expires
   - Store timer state in localStorage (survives page refresh)

2. **Question Navigation**:
   - Show question counter: "Question 3 of 15"
   - Display all questions in one scrollable page OR
   - Show one question at a time with Previous/Next buttons
   - Mark answered questions with checkmark icon
   - Highlight unanswered questions

3. **Question Rendering**:
   - **MCQ**: Radio buttons for options, only one selectable
   - **Short Answer**: Textarea with character counter
   - **Cloze**: Input fields for each blank

4. **Progress Tracking**:
   - Progress bar showing completion percentage
   - List of questions with status (answered/unanswered)
   - "Submit Exam" button (only enabled when all questions answered)

5. **Confirmation Dialog**:
   - Before submitting: "Are you sure? You have X unanswered questions."
   - On time expiry: "Time's up! Submitting your exam..."

**Results Screen**:
1. **Score Display**:
   - Large percentage score with pass/fail indicator
   - Visual: Green checkmark for pass, red X for fail
   - Time taken: "Completed in 23:45"

2. **Statistics Section**:
   - Overall: "12/15 correct (80%)"
   - By question type:
     - Multiple Choice: 5/6 correct (83%)
     - Short Answer: 4/5 correct (80%)
     - Cloze: 3/4 correct (75%)

3. **Question Review**:
   - For each question, show:
     - Question text
     - Your answer
     - Correct answer (for MCQ and Cloze)
     - AI feedback (for short answer)
     - Correctness indicator (✓ or ✗)
     - Time spent on question

4. **Actions**:
   - "Retake Exam" button (creates new session)
   - "Return to Deck" button
   - "Review Incorrect Answers" button (adds incorrect cards to flagged list)

### 3. Exam Mode UI/UX Requirements

**Restrictions**:
- Disable navigation away from exam page (show warning dialog)
- Prevent browser back button during exam
- Lock answers after submission (no editing)
- No "Show Answer" button (unlike practice mode)

**Accessibility**:
- Keyboard navigation (Tab, Enter, Arrow keys)
- Screen reader support for timer and progress
- High contrast mode for timer warning
- Focus management for question navigation

**Responsive Design**:
- Mobile-friendly layout
- Adjust timer and progress bar for small screens
- Ensure textarea inputs work on mobile

### 4. AI Evaluation Logic

**Prompt Engineering for Short Answers**:
```
You are evaluating a student's short answer response.

Question: {question}
Expected Answer: {expected_answer}
Student's Answer: {user_answer}

Evaluate the student's answer on a scale of 0-100 based on:
1. Correctness: Does it answer the question accurately?
2. Completeness: Does it cover the key points?
3. Clarity: Is it well-articulated?

Provide:
- Score (0-100)
- Brief feedback (2-3 sentences)

Output as JSON: {"score": 85, "feedback": "..."}
```

**Grading Rubric**:
- 90-100: Excellent, comprehensive answer
- 70-89: Good, covers main points
- 50-69: Partial, missing key details
- 0-49: Incorrect or off-topic

**Error Handling**:
- If AI service fails, default to manual grading (mark as "Needs Review")
- Show error message: "AI evaluation unavailable, answer marked for manual review"
- Allow instructor override (future enhancement)

### 5. Success Criteria

**Functionality**:
- [ ] Exam mode only includes MCQ, Short Answer, and Cloze cards
- [ ] Basic type cards are automatically excluded
- [ ] Cannot submit exam until all questions answered
- [ ] Timer counts down correctly and auto-submits on expiry
- [ ] MCQs are auto-graded immediately
- [ ] Short answers are evaluated by AI with feedback
- [ ] Cloze answers are compared to expected text
- [ ] Final score is calculated correctly
- [ ] Results screen shows detailed breakdown

**User Experience**:
- [ ] Exam flow is intuitive and clear
- [ ] Progress is visible at all times
- [ ] Timer is non-intrusive but noticeable
- [ ] Submission confirmation prevents accidental submits
- [ ] Results are comprehensive and helpful
- [ ] AI feedback is constructive and accurate

**Technical**:
- [ ] Exam state persists on page refresh (localStorage)
- [ ] AI evaluation handles edge cases gracefully
- [ ] Backend validates all answers before scoring
- [ ] Exam session cannot be resumed after completion
- [ ] All exam data is properly stored in database

**Testing**:
- [ ] Write integration test for full exam flow
- [ ] Test timer functionality (countdown, auto-submit)
- [ ] Test AI evaluation with various answer qualities
- [ ] Test edge cases (empty answers, time expiry, network failures)
- [ ] Test all question types in exam context

### 6. Deliverables

1. **Code Implementation**:
   - All three Milestone 2 streams completed
   - Exam mode backend endpoints
   - Exam mode frontend components
   - AI evaluation integration
   - Comprehensive test coverage

2. **Documentation**:
   - User guide for taking exams
   - Explanation of AI evaluation criteria
   - Screenshots of exam flow
   - Technical documentation for exam mode architecture

3. **Demo**:
   - Video demonstration showing:
     - Creating a deck with complex question types
     - Starting an exam session
     - Answering all question types
     - Timer functionality
     - Submitting and viewing results
     - AI feedback on short answers

### 7. Grading Rubric for Extra Credit

**Implementation Quality** (40 points):
- All three streams fully implemented (15 points)
- Exam mode backend complete (10 points)
- Exam mode frontend complete (10 points)
- AI evaluation integrated (5 points)

**User Experience** (25 points):
- Intuitive UI/UX (10 points)
- Proper error handling (5 points)
- Responsive design (5 points)
- Accessibility considerations (5 points)

**Technical Excellence** (20 points):
- Clean, maintainable code (10 points)
- Comprehensive testing (10 points)

**Documentation** (15 points):
- Clear user documentation (7 points)
- Technical documentation (5 points)
- Demo video/guide (3 points)

**Total**: 100 points extra credit